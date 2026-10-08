# 🏛️ WordPress to Sanity Vault

[![CultureOS Labs](https://img.shields.io/badge/Maintained%20by-CultureOS%20Labs-000000?style=for-the-badge&logo=cloudflare&logoColor=orange)](https://cultureos.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-0%20External%20Deps-success?style=for-the-badge)](#-zero-external-dependencies)
[![Non-Profit Ready](https://img.shields.io/badge/Non--Profit-Friendly-8A2BE2?style=for-the-badge)](#-why-this-exists-the-problem-we-solve)

**Open-source WordPress to Sanity migration toolkit for museums, art foundations, and cultural archives. AI-assisted archival curation by CultureOS Labs.**

> Designed for cultural foundations, museums, artist estates, research libraries, and non-profit institutions migrating 10–20 years of legacy WordPress archives into [Sanity Headless CMS](https://sanity.io) and modern Next.js/Astro architectures. Available both as an agentic conversational workflow and standalone Python scripts.

Developed and maintained by **[CultureOS Labs](https://cultureos.dev)** — the research arm of **[CultureOS](https://cultureos.dev)**, an AI-native practice for cultural institutions. Learn more on our [official project page](https://cultureos.dev/open-source/wordpress-to-sanity).

---

## 🌟 Why This Exists (The Problem We Solve)

Migrating legacy WordPress sites (thousands of articles, complex media attachments, and 15+ years of historical taxonomy) into a modern Headless CMS is notoriously challenging for mission-driven organizations:

- **Prohibitive Migration Quotes**: Commercial agency estimates for bespoke archival data migration frequently range from **$30,000 to $100,000**, with timelines spanning 3 to 6 months.
- **The "Terminal Barrier"**: Curators, archivists, and directors often lack software engineering backgrounds. Forcing non-technical staff to navigate Node.js runtime environments, npm build failures, or command-line scripts introduces friction and halts progress.
- **SEO & Provenance Risk**: Decades of incoming scholarly citations, search engine authority, and organic backlinks are jeopardized when legacy URLs (e.g. `/?p=14092` or ambiguous slugs like `/exhibition-2`) break without permanent 301 redirects.
- **Taxonomy Decay**: After 10–20 years of editorial churn, WordPress archives often accumulate hundreds of redundant tags and overlapping categories that degrade collections discoverability.

**WordPress to Sanity Vault** solves these challenges by combining an empathetic, conversational AI curation protocol with pure-Python ingestion scripts that run out of the box with **zero third-party dependencies**.

---

## 👥 Who This Project Is For

- **Museums & Art Galleries**: Transitioning public programs, past exhibitions, and curatorial announcements from legacy monoliths to modern headless web architectures.
- **Artist Foundations & Estates**: Preserving decades of documented history, essays, and press archives with verified metadata integrity.
- **Research Libraries & Digital Archivists**: Cleaning up chaotic folksonomies into structured, machine-readable taxonomies.
- **WordPress & Sanity Developers**: Seeking a clean, tested pipeline to export WordPress XML/JSON into Sanity NDJSON and TypeScript schemas without building one-off custom scrapers.

---

## ✨ Key Technical Capabilities

### 1. 🤖 Dynamic Concierge Onboarding
Interact conversationally in plain English. In an AI assistant environment (Google Antigravity, Claude Desktop, or OpenAI ChatGPT), the agent acts as your digital archivist:
- Welcomes your team and establishes institutional identity, collection size, and migration scope.
- Ingests standard WordPress XML exports (`export.xml`), JSON dumps, or REST API endpoints.
- Scans legacy categories and tags to identify duplicates, orphans, and historical inconsistencies.

### 2. 🧠 AI Taxonomy Synthesis
Rather than blindly carrying over 20 years of editorial clutter, the engine evaluates your archive and recommends:
- **5–8 Clean Core Categories** aligned with cultural heritage standards (e.g., *Exhibitions*, *Permanent Collection*, *Artist Fellowships*, *Public Programs*).
- **Domain-Specific Tag Normalization** tailored to your institutional focus.
- Interactive conversational review: approve, rename, merge, or adjust categories in real time before writing records.

### 3. 🛡️ Substack-Standard Collision-Free Slugs & 301 Map
Adopts the proven `/archive/[ID]-[Semantic-Slug]` dual-track URL pattern:
- **Collision-Free Structure**: Ensures every post has a guaranteed unique slug even when historic titles collide (e.g., annual exhibitions sharing identical names across multiple years).
- **SEO & Citation Preservation**: Automatically generates a 1:1 `slug_redirects_map.json` containing permanent 301 redirect rules compatible with Cloudflare Workers, Next.js redirects, or Vercel middleware.

### 4. 🚀 Zero-CLI Direct Sanity Cloud Ingestion
For lean teams without an in-house engineering team:
- Provide your Sanity **Project ID**, **Dataset**, and a **Write API Token**.
- `scripts/sanity_direct_sync.py` uses standard HTTP to push documents straight to Sanity Cloud via the official Mutation API.
- Built-in polite throttling and automatic retry logic on HTTP 429 rate limits.
- Inspect records immediately in Sanity Studio at `https://<your-project>.sanity.studio`.

### 5. 📦 Offline Developer Mode (NDJSON + TypeScript)
For development and devops workflows:
- Generates standard `sanity_export.ndjson` for instant bulk loading via `npx sanity dataset import`.
- Automatically emits production-ready TypeScript document schemas (`post.ts`) matching Sanity Studio v3 standards.

---

## ⚡ Zero External Dependencies

To ensure students, volunteers, and curators can run this tool without package conflicts:

- **No `pip install` required**: Uses only Python 3.8+ standard library modules (`urllib.request`, `json`, `os`, `sys`, `time`, `argparse`).
- **No `npm install` required**: Direct cloud ingestion operates over pure HTTPS REST mutations.

---

## 🚀 Installation & Usage Workflows

### Workflow A: Agentic Conversational Curation (Recommended for Curators)

If you use **Google Antigravity**, **Claude Desktop**, or **ChatGPT Codex**:

1. Clone or download this repository:
   ```bash
   git clone https://github.com/culture-os-labs/wordpress-to-sanity-vault.git
   ```
2. Reference `SKILL.md` in your AI environment or ask your agent:
   > *"I have a 10-year WordPress archive from our art foundation that I need to migrate to Sanity. Can you guide me through the cleanup?"*
3. Provide your WordPress `export.xml` or JSON dump. The agent will parse your records, synthesize a modern taxonomy, generate redirect maps, and prepare documents for ingestion.

---

### Workflow B: Standalone Python Ingestion (For Developers)

#### 1. Ingest Directly into Sanity Cloud via HTTPS Mutation
Push sanitized records directly into your Sanity dataset:

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

## ⚠️ Known Limitations & Considerations

- **Custom Fields (ACF / Meta Boxes)**: The default schema and ingestion scripts map standard WordPress attributes (titles, dates, slugs, categories, tags, excerpts, body content, and hero images). Highly customized Advanced Custom Fields (ACF) or complex repeater fields require adding custom field definitions to the schema generator.
- **High-Volume Media Libraries**: For archives containing tens of thousands of high-resolution images, we recommend running asset ingestion in staggered batches to stay within Sanity Asset API bandwidth and rate quotas.
- **Custom URL Rewrite Structures**: Non-standard permalink configurations (such as date-based archives or custom query strings) should be verified against `slug_redirects_map.json` prior to production DNS cutover.
- **Sanity API Token Permissions**: Direct ingestion requires a Sanity token with Write permissions. Never commit API tokens to version control.

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

**[CultureOS](https://cultureos.dev)** is an AI-native practice dedicated to cultural institutions, smaller museums, artist foundations, and research archives. We modernize systems from everyday workflows to cloud infrastructure and scholarly intelligence.

### Related Offerings & Research:
- **[Infrastructure Upgrade](https://cultureos.dev/what-we-do/infrastructure)** — Server recovery, cloud migration, automated backups, and system hardening for cultural institutions.
- **[Digital Transformation](https://cultureos.dev/what-we-do/digital-transformation)** — Rebuilding websites, CMS platforms, donor records, and communications on maintainable systems.
- **[Institutional Diagnostic](https://cultureos.dev/what-we-do/diagnostic)** — Comprehensive systems review, workflow mapping, and an executable technology roadmap.
- **[Open Cultural Evidence Framework](https://cultureos.dev/labs/open-framework)** — Research methodology for source-grounded cultural intelligence (DOI: [10.5281/zenodo.22828367](https://doi.org/10.5281/zenodo.22828367)).
- **[Tom of Finland Foundation Pilot](https://cultureos.dev/work/tom-of-finland-foundation)** — Our founding laboratory in Los Angeles modernizing collections and catalogue research.

**Contact & Inquiries**:
- Website: [https://cultureos.dev](https://cultureos.dev)
- Project Page: [https://cultureos.dev/open-source/wordpress-to-sanity](https://cultureos.dev/open-source/wordpress-to-sanity)
- Email: [hello@cultureos.dev](mailto:hello@cultureos.dev)
- GitHub Organization: [https://github.com/culture-os-labs](https://github.com/culture-os-labs)

---

## 🤝 Contributing & Community

We welcome contributions from digital archivists, museum technologists, and developers!
- To report a bug or request an enhancement, please [open an issue](https://github.com/culture-os-labs/wordpress-to-sanity-vault/issues).
- Pull requests are reviewed with a focus on code readability, accessibility, and zero-dependency maintenance.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Copyright © 2026 **CultureOS Labs** ([https://cultureos.dev](https://cultureos.dev)) & Nolan Feng.
