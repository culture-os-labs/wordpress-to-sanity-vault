# 🏛️ WordPress to Sanity Vault

[![CultureOS Labs](https://img.shields.io/badge/Maintained%20by-CultureOS%20Labs-000000?style=for-the-badge&logo=cloudflare&logoColor=orange)](https://cultureos.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20External%20Deps-success?style=for-the-badge)](#-zero-external-dependencies)
[![Non-Profit Ready](https://img.shields.io/badge/Non--Profit-Friendly-8A2BE2?style=for-the-badge)](#-why-this-exists-the-problem-we-solve)

**The Agent-Native, Zero-CLI Archival Curation & Migration Engine from Legacy WordPress to Sanity Studio.**

> Built for cultural foundations, museums, art archives, research libraries, and non-profit institutions who need to migrate 10–20 years of legacy WordPress archives into [Sanity Headless CMS](https://sanity.io) and modern Next.js/Astro architectures — **without hiring an agency or touching a command line.**

Developed and openly maintained by **[CultureOS Labs](https://cultureos.dev)** — an AI-native practice & research arm for cultural institutions.

---

## 🌟 Why This Exists (The Problem We Solve)

Migrating legacy WordPress sites (thousands of posts, complex media attachments, and 15+ years of technical debt) into a modern Headless CMS is notoriously painful for mission-driven organizations:

- **Prohibitive Agency Fees**: Agencies routinely quote **\$30,000 – \$100,000** and take 3–6 months for bespoke data migration.
- **The "Terminal Barrier"**: Curators, archivists, and foundation directors are non-technical. Forcing them to navigate Node.js versions, npm build errors, and command-line scripts creates intense friction.
- **SEO & Provenance Risk**: 15 years of incoming academic citations and organic backlinks are destroyed when legacy URLs (e.g. `/?p=14092` or collision-prone slugs like `exhibition-2`) break.

**WordPress to Sanity Vault** eliminates this barrier. It transforms the migration into a **gentle, empathetic conversational interview inside your AI assistant** (Google Antigravity, Claude Desktop, or OpenAI ChatGPT), backed by pure-Python ingestion scripts that require **zero external dependencies**.

---

## ✨ Key Capabilities

### 1. 🤖 Dynamic Concierge Onboarding
Interact in plain English. The AI agent acts as your digital archivist:
- Welcomes you and establishes your foundation's identity and goals.
- Accepts standard WordPress XML exports (`export.xml`), JSON dumps, or live site feeds via simple drag-and-drop.
- Identifies decade-old categories and noisy tags.

### 2. 🧠 AI Taxonomy Synthesis
Instead of migrating 20 years of chaotic, duplicate categories, the engine samples your archive and proposes:
- **5–8 Elegant Core Categories** (e.g., *Exhibitions*, *Permanent Collection*, *Artist Fellowships*, *Public Programs*).
- **Multi-Dimensional Tag Filtering** tailored to your institutional domain.
- Full conversational review: rename, merge, or adjust categories in real time.

### 3. 🛡️ Substack-Standard 0-Collision Slugs
Adopts the battle-tested `/archive/[ID]-[Semantic-Slug]` dual-track pattern:
- Guarantees 100% collision-free URLs, even when articles share identical historic titles.
- Automatically generates a 1:1 `slug_redirects_map.json` with 301 permanent redirect rules ready for Cloudflare Workers, Vercel, or Next.js middleware.

### 4. 🚀 Zero-CLI Direct Sanity Cloud Ingestion
For non-technical teams with no developer on staff:
- Provide your Sanity **Project ID**, **Dataset**, and a **Write Token**.
- `scripts/sanity_direct_sync.py` uses pure HTTP to push documents straight into Sanity Cloud via the official Mutation API.
- Open your browser at `https://<your-project>.sanity.studio` and your entire archive is already live!

### 5. 📦 Offline Developer Mode (NDJSON + TypeScript)
For engineering teams:
- Generates `sanity_export.ndjson` for instant bulk loading via `npx sanity dataset import`.
- Automatically outputs modern Sanity Studio v3 TypeScript schemas (`post.ts`).

---

## ⚡ Zero External Dependencies

To guarantee that any non-profit, student, or volunteer can run this tool on any computer without environment breakage:

```bash
# No pip install required!
# No npm install required!
# Uses only standard library modules: urllib, json, os, sys, time, argparse
```

---

## 🚀 Quick Start Guide

### Method A: Use with AI Agents (Recommended for Curators)

If you use **Google Antigravity**, **Claude Desktop**, or **ChatGPT Codex**:

1. Clone or download this repository.
2. In your AI client, provide `SKILL.md` or invoke the skill:
   > *"I have a 10-year WordPress archive from our art foundation that I need to migrate to Sanity. Can you guide me through the cleanup?"*
3. Drop your `export.xml` file into the chat. The agent will autonomously parse, synthesize modern taxonomy, and prepare your documents for ingestion.

---

### Method B: Standalone Command-Line Ingestion (For Developers)

#### 1. Ingest Directly into Sanity Cloud via Pure HTTP
Push your sanitized records directly into your Sanity Studio dataset:

```bash
python3 scripts/sanity_direct_sync.py \
  --project-id "YOUR_PROJECT_ID" \
  --dataset "production" \
  --token "skYOUR_SANITY_WRITE_TOKEN" \
  --data data/sample_posts.json \
  --batch-size 50
```

#### 2. Export Offline NDJSON Bundle & TypeScript Schema
Generate an offline `.ndjson` bundle and a ready-to-use Sanity v3 `post.ts` schema:

```bash
python3 scripts/sanity_ndjson_exporter.py \
  --data data/sample_posts.json \
  --output exports
```

Output files created:
- `exports/sanity_export.ndjson` — Ready for `npx sanity dataset import`
- `exports/post.ts` — Production-grade Sanity Studio schema

---

## 🗂️ Repository Architecture

```text
wordpress-to-sanity-vault/
├── SKILL.md                          # Full Agentic Workflow & Curatorial Protocol
├── README.md                         # Master Documentation
├── LICENSE                           # Open Source MIT License
├── requirements.txt                  # Dependency notice (Standard library only)
├── .gitignore                        # Git ignore rules
├── data/
│   └── sample_posts.json             # Sample cultural foundation dataset for testing
└── scripts/
    ├── sanity_direct_sync.py         # Pure HTTP Sanity Cloud Mutation Uploader
    └── sanity_ndjson_exporter.py     # Offline NDJSON exporter & TypeScript schema generator
```

---

## 🏛️ About CultureOS Labs

**[CultureOS](https://cultureos.dev)** is an AI-native consultancy and technology practice dedicated to the cultural sector. We partner with museums, art foundations, artist estates, and non-profit institutions to modernize their digital presence, safeguard digital provenance, and build intelligent infrastructure.

### Our Practices:
1. **[The Reading](https://cultureos.dev)** — Fixed-scope digital diagnostic audit for institutions.
2. **[Front of House](https://cultureos.dev)** — Next-generation visitor experiences, online collections, and responsive design systems.
3. **[Back of House](https://cultureos.dev)** — Archival digitization pipelines, Catalogues Raisonnés, and Headless CMS modernization.

- **Official Website**: [https://cultureos.dev](https://cultureos.dev)
- **GitHub Organization**: [https://github.com/culture-os-labs](https://github.com/culture-os-labs)
- **Inquiries & Non-Profit Assistance**: [hello@cultureos.dev](mailto:hello@cultureos.dev)

---

## 🤝 Contributing & Community

We warmly welcome contributions from cultural technologists, archivists, and open-source contributors!
- To report a bug or suggest a feature, please [open an issue](https://github.com/culture-os-labs/wordpress-to-sanity-vault/issues).
- For non-profit advisory, migration partnerships, or institutional pilots, contact us at [hello@cultureos.dev](mailto:hello@cultureos.dev).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Copyright © 2026 **CultureOS Labs** ([https://cultureos.dev](https://cultureos.dev)) & Nolan Feng.
