#!/usr/bin/env python3
"""
Sanity Direct Sync: Pure HTTP Sanity Cloud Mutation Uploader
============================================================
Part of the WordPress-to-Sanity Vault Migration Engine.
Developed & Maintained by CultureOS Labs (https://cultureos.dev).

Features:
---------
- 100% Zero-CLI & Zero-Dependency: Uses Python standard library only (urllib, json, time).
- Direct HTTP Mutation: Pushes documents straight into Sanity Cloud via Mutation API.
- No Node.js, npm, or @sanity/cli required.
- Polite throttling & automatic retry on rate limits (HTTP 429).
- Live progress indicators and timestamp normalization.

Contact: hello@cultureos.dev
License: MIT
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
import time

def sync_to_sanity(project_id, dataset, token, data_file, batch_size=50):
    if not os.path.exists(data_file):
        print(f"❌ Error: Data file not found: {data_file}")
        sys.exit(1)

    with open(data_file, "r", encoding="utf-8") as f:
        posts = json.load(f)

    total = len(posts)
    print("=" * 65)
    print("🏛️  CultureOS Labs — Sanity Cloud Direct Ingestion Engine")
    print(f"   Target Project ID: {project_id}")
    print(f"   Target Dataset   : {dataset}")
    print(f"   Total Records    : {total:,}")
    print(f"   Batch Size       : {batch_size}")
    print("=" * 65)

    url = f"https://{project_id}.api.sanity.io/v2021-06-07/data/mutate/{dataset}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "CultureOS-Vault-Migrator/1.0 (+https://cultureos.dev)"
    }

    success_count = 0
    start_time = time.time()

    # Process in batches
    for i in range(0, total, batch_size):
        chunk = posts[i:i + batch_size]
        mutations = []

        for p in chunk:
            post_id = p.get("ID") or p.get("legacyId")
            title = p.get("Clean Title") or p.get("Title") or "Untitled Post"
            slug = p.get("CanonicalSlug") or p.get("Slug") or str(post_id)
            date = p.get("Date") or "2026-01-01"
            if len(date) == 10:
                date = f"{date}T12:00:00Z"
            elif not date.endswith("Z"):
                date = f"{date}Z"

            doc = {
                "_id": f"post-{post_id}",
                "_type": "post",
                "title": title,
                "slug": {"_type": "slug", "current": slug},
                "publishedAt": date,
                "category": p.get("Category") or "General",
                "tags": p.get("Tags") or [],
                "excerpt": p.get("Excerpt") or "",
                "legacyId": post_id,
            }

            img = p.get("First High-Res Image") or p.get("FullImg") or p.get("Thumb")
            if img:
                doc["legacyHeroImageUrl"] = img

            mutations.append({"createOrReplace": doc})

        payload = json.dumps({"mutations": mutations}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

        retries = 3
        while retries > 0:
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    if resp.status in (200, 201):
                        success_count += len(chunk)
                        progress = (success_count / total) * 100
                        print(f"   ✓ Batch {i // batch_size + 1:>3}: Synced {success_count:>5}/{total} documents ({progress:.1f}%)")
                        break
                    else:
                        print(f"   ⚠️ Unexpected status {resp.status}, retrying...")
            except urllib.error.HTTPError as e:
                err_body = e.read().decode("utf-8")
                print(f"   ❌ HTTP Error {e.code}: {err_body}")
                if e.code == 429: # Rate limit
                    time.sleep(2)
                retries -= 1
            except Exception as e:
                print(f"   ❌ Network error: {e}")
                retries -= 1
                time.sleep(1)

        time.sleep(0.15) # Polite throttle to prevent Cloudflare/Sanity rate limits

    elapsed = time.time() - start_time
    print("-" * 65)
    print(f"🎉 Ingestion Complete! Successfully pushed {success_count:,} / {total:,} documents in {elapsed:.1f}s.")
    print(f"👉 Studio Access: https://{project_id}.sanity.studio/")
    print(f"🏛️  Powered by CultureOS Labs (https://cultureos.dev)\n")

def main():
    parser = argparse.ArgumentParser(
        description="Directly sync WordPress archive into Sanity Cloud via Mutation API. Maintained by CultureOS Labs (https://cultureos.dev)."
    )
    parser.add_argument("--project-id", required=True, help="Sanity Project ID (e.g., uo5i76py)")
    parser.add_argument("--dataset", default="production", help="Sanity Dataset (default: production)")
    parser.add_argument("--token", required=True, help="Sanity Write API Token (sk...)")
    parser.add_argument("--data", default="data/sample_posts.json", help="Path to sanitized JSON dataset")
    parser.add_argument("--batch-size", type=int, default=50, help="Batch size per mutation request (default: 50)")
    args = parser.parse_args()

    sync_to_sanity(args.project_id, args.dataset, args.token, args.data, args.batch_size)

if __name__ == "__main__":
    main()
