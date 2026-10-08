---
name: wordpress-to-sanity-vault
description: >
  Autonomous end-to-end migration, curation, and URL restructuring pipeline
  from legacy WordPress to Sanity Studio and modern Next.js/Astro stacks.
  Developed by CultureOS Labs (https://cultureos.dev) for non-technical curators,
  cultural foundations, art galleries, and digital archives. Features conversational
  dynamic onboarding, AI taxonomy synthesis, Substack-standard 0-collision slug
  generation, and zero-CLI direct Sanity Cloud ingestion.
---

# 🏛️ WordPress to Sanity Vault Migration Skill
*Transform messy 10–20 year WordPress archives into pristine Sanity Studio collections with zero technical jargon.*

**Developed & Maintained by [CultureOS Labs](https://cultureos.dev)**  
*Contact & Curatorial Inquiries: [hello@cultureos.dev](mailto:hello@cultureos.dev)*

---

## 🌟 Philosophy & Core Principles

1. **Empathy First (No Technical Jargon)**: Most users are non-technical curators, archive directors, or marketing leads. Never overwhelm them with raw terminal commands, cryptic stack traces, or node dependency conflicts.
2. **Dynamic Concierge Onboarding**: Always walk the user through a gentle, step-by-step conversational interview before executing heavy scripts. Confirm brand identity, archive scope, and AI-suggested categories.
3. **In-Client Visual Studio**: The generated review studio renders directly inside the user's AI client (Google Antigravity Webview, Claude Desktop Artifacts, or ChatGPT Canvas) so the curator never leaves the conversation.
4. **Substack-Standard 0-Collision Slugs**: All URLs adopt the durable dual-track pattern `/archive/[ID]-[Semantic-Slug]`, paired with an automated 1:1 301 permanent redirect map to protect decades of organic search reputation.
5. **Zero-CLI Direct Sanity Cloud Ingestion**: Support pushing directly to Sanity via pure HTTP Mutation API using standard library tools, completely bypassing the need for Node.js, `@sanity/cli`, or local developer configuration.

---

## 🧭 The 5-Step Curatorial Journey

### Step 1: Institutional Discovery & Scope
When a user expresses a need to migrate or clean up an old WordPress site, warmly welcome them:
> "Hello! We would love to help you safely migrate and polish your historical archive into a modern, beautifully structured home. To ensure everything is tailored to your organization:
> 1. **What is the name of your foundation, gallery, or archive?** (e.g., *Tom of Finland Foundation*, *Anthology Film Archives*)
> 2. **What is your primary milestone?** (e.g., *Migrating to Sanity Studio*, *launching an editorial redesign*, or *resolving 15 years of messy tags*?)"

### Step 2: WordPress Source Ingestion
Offer three simple, non-intimidating options for ingesting the archive:
> "Where is your historical WordPress content currently located?
> - **Option A: I have an export file** (e.g., `.xml` from WordPress *Tools ➔ Export*, `.json`, or a database dump) 👉 *Simply drag and drop the file directly into our chat window!*
> - **Option B: I have the live site URL and credentials** 👉 *Share the URL and temporary login; we will safely extract your published posts and media records.*
> - **Option C: I need guidance exporting** 👉 *No worries at all! Log into your WordPress dashboard, click `Tools` on the left sidebar, select `Export`, and choose 'All Content'. Then drop that file right here.*"

### Step 3: AI Taxonomy Synthesis & Approval
Once the archive is parsed:
1. Sample 25–50 articles across various publication years.
2. Present a refined, domain-specific taxonomy:
   - 5–8 high-level core categories (consolidating decades of tag sprawl).
   - 2–4 orthogonal metadata dimensions (e.g., *Exhibitions*, *Permanent Collection*, *Artist Fellowships*, *Public Programs*).
3. Confirm with the curator:
   > "We analyzed your archive of **[X]** historical posts. Decades of edits produced [Y] redundant tags. We propose streamlining them into **[N] core institutional categories**:
   > 1. Category A — *Description*
   > 2. Category B — *Description*...
   > 
   > How do these categories feel to your team? You can rename, merge, or adjust any of them right now."

### Step 4: Visual Curation Studio Preview
Once approved:
1. Normalize HTML markup, strip deprecated inline styling, and isolate high-resolution hero images.
2. Format slugs using the Substack standard (`/archive/[ID]-[Semantic-Slug]`).
3. Launch the responsive visual curation card grid directly in the client:
   - Antigravity: Interactive Webview.
   - Claude Desktop: Artifacts View.
   - ChatGPT / Codex: Visual Canvas.
4. Guide the review process:
   > "✨ Your interactive Content Vault is ready to explore!
   > - Filter by category or search by keyword.
   > - Click any card to inspect full-resolution assets and typography.
   > - Click `Keep` or `Discard` to curate the final ingestion set."

### Step 5: Sanity Cloud Ingestion Handoff
When the curation review is complete:
> "Are you ready to synchronize these curated documents into Sanity Studio?
> - **Direct Cloud Push (Zero Developer Required)**:
>   Provide your **Project ID**, **Dataset** (usually `production`), and a **Write API Token**. Our automated engine pushes all records directly into your Sanity database via secure HTTP.
> - **Offline Developer Bundle**:
>   We export a complete `sanity_export.ndjson`, the production TypeScript schema (`post.ts`), and the 301 permanent redirect map for your Next.js / Astro front-end."

---

## 🛠️ Included Production Tooling

All underlying scripts are located in `scripts/` and run on **pure Python standard library** (Zero external dependencies!):

### 1. `sanity_direct_sync.py` (Pure HTTP Mutation Engine)
Pushes sanitized documents directly into Sanity Cloud via REST API without Node.js or `@sanity/cli`:
```bash
python3 scripts/sanity_direct_sync.py \
  --project-id "uo5i76py" \
  --dataset "production" \
  --token "sk..." \
  --data data/sample_posts.json
```

### 2. `sanity_ndjson_exporter.py` (Offline NDJSON & Schema Generator)
Generates offline import packages and ready-to-use TypeScript schemas:
```bash
python3 scripts/sanity_ndjson_exporter.py \
  --data data/sample_posts.json \
  --output exports/
```

---

## 🏛️ About CultureOS Labs

This Skill is an open-source initiative created by **[CultureOS Labs](https://cultureos.dev)**.

CultureOS is an AI-native practice and research arm dedicated to cultural institutions, art foundations, museums, and historical archives. We build intelligent infrastructure, cataloguing pipelines, and modern visitor experiences that honor institutional heritage while leveraging modern technology.

- **Website**: [https://cultureos.dev](https://cultureos.dev)
- **Practice & Advisory**: [https://cultureos.dev#practices](https://cultureos.dev)
- **Contact & Partnerships**: [hello@cultureos.dev](mailto:hello@cultureos.dev)
- **GitHub Organization**: [https://github.com/culture-os-labs](https://github.com/culture-os-labs)

---

## 📄 License
MIT License. Free and open for non-profit institutions, universities, and commercial agencies alike.
