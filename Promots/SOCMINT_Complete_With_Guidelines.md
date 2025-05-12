# SOCMINT Implementation Prompts + General Guidelines

# General Development Guidelines (Must-Follow)

1. **Only make the exact changes I request** — do not modify, remove, or alter any other code, styling, or page elements unless explicitly instructed. If my request conflicts with existing code or functionality, pause and ask for confirmation before proceeding. Always follow this rule.

2. **Before you generate any code**, explain exactly what you plan to do. Include affected files, components, and edge cases. Wait for my confirmation before proceeding.

3. **You are my AI pair programmer.** I want to build [FEATURE]. Break this into steps and outline a build plan. Label each step clearly and tell me when you're ready to begin. Wait for my go-ahead.

4. **Generate a reusable UI kit** using [ShadCN / Tailwind / Custom CSS]. Include button styles, typography, input fields, and spacing tokens. Keep it consistent, clean, and minimal.

5. **Generate a complete test suite** for this function/module. Include edge cases, invalid inputs, and expected outputs. Label each test and include comments explaining the logic.

6. **Profile this code for bottlenecks.** Suggest two optimizations labeled 'Option A' and 'Option B' with trade-offs. Focus on real-world scenarios, not micro-optimizations.

7. **Write a complete README** for this project, including installation, usage, commands, and deployment steps. Assume the reader is a solo indie dev. Add emoji callouts if helpful.

8. **From now on, follow these coding conventions:** [list your rules]. Stick to them in every file unless told otherwise. Ask if anything is unclear.

9. **Generate a clean, responsive HTML + CSS starter** with no dependencies. Include a homepage, about page, and contact form. Design should be minimalist, centered layout, mobile-first.

10. **Here's a prompt I want to improve:** [PASTE PROMPT]. Rewrite it to be more effective, clearer, and more consistent. Explain what you changed and why.


---

# SOCMINT SaaS AI Prompts - Full Implementation Guide

**Prepared:** 2025-05-07 02:48:46 UTC  
**Format:** Ready for GPT-4.1 / TRAE / Engineering SOPs  
**Project:** SOCMINT - Digital Investigations & Social Intelligence SaaS Platform

---

## Table of Contents

1. [AI Prompt 1 - Infrastructure with Docker Compose](#prompt-1)
2. [AI Prompt 2 - Data Collector (Social APIs + Web Scraping)](#prompt-2)
3. [AI Prompt 3 - AI/NLP Analytics Service](#prompt-3)
4. [AI Prompt 4 - Financial Crime Detection Service](#prompt-4)
5. [AI Prompt 5 - Cyber Forensics & Blockchain Logging](#prompt-5)
6. [AI Prompt 6 - Flutter Frontend with UAE PASS & Localization](#prompt-6)
7. [AI Prompt 7 - Full Integration, Testing, and Deployment](#prompt-7)
8. [AI Prompt 8 - Social Media Manager (Postiz Integration)](#prompt-8)

---

## Prompt 1
Create a full infrastructure layout for a multi-container SOCMINT SaaS platform using Docker Compose... [Content trimmed here for brevity]

---

## Prompt 2
Create a complete FastAPI microservice named `data_collector` inside `backend/data_collector/`... [Content trimmed here for brevity]

---

## Prompt 3
Create a FastAPI microservice named `ai_analytics_service` inside `backend/ai_analytics_service/`... [Content trimmed here for brevity]

---

## Prompt 4
Create a FastAPI microservice named `financial_crime_service` inside `backend/financial_crime_service/`... [Content trimmed here for brevity]

---

## Prompt 5
Create a FastAPI microservice named `cyber_forensics_service` inside `backend/cyber_forensics_service/`... [Content trimmed here for brevity]

---

## Prompt 6
Create a complete Flutter Web application named `socmint_dashboard` for the SOCMINT platform... [Content trimmed here for brevity]

---

## Prompt 7
Create a full deployment and testing checklist for the SOCMINT SaaS platform using Docker Compose... [Content trimmed here for brevity]

---

## Prompt 8
Integrate `Postiz App` from GitHub into the SOCMINT platform as a standalone microservice called `social_media_manager`... [Content trimmed here for brevity]

---
---

## Prompt 9: Visual Identity System for SOCMINT by RHAL

Design a complete visual identity system for the SOCMINT platform under the branding of "RHAL – عجمان للتقنيات المتقدمة".

Use the provided logo as the main reference. The identity must be simple, modern, UAE-inspired, and technically oriented.

### Required Deliverables:

1. **Color Palette**
   - Primary: Exact green from the logo.
   - Secondary: White, black, soft gray.
   - Accent: Emirati flag red for alerts.

2. **Typography**
   - Arabic: Noto Kufi Arabic or Dubai Font.
   - English: Montserrat or Source Sans Pro.
   - Bold headings, light body text.

3. **UI Component Styles**
   - Rounded buttons with green glow.
   - Minimalist cards with slight shadow.
   - Sidebar with green highlights.

4. **Logo Usage Rules**
   - Always use green bar above "رحّال".
   - Primary logo on black background.
   - Respect safe spacing around logo.

5. **Dashboard Layout**
   - Left dark sidebar, top app bar.
   - Main grid for data visualizations.
   - Prefer dark mode default.

6. **Landing Page Design**
   - Hero with centered logo and tagline.
   - Sections: About, Benefits, Dashboard, Subscribe.
   - Language switch (ar/en) top-right.

7. **Document Style Guide**
   - Logo usage variants.
   - Font size hierarchy.
   - PDF/report templates.

8. **Favicon & App Icon**
   - Square version of logo.
   - 512x512, 192x192, 48x48 sizes.

### Notes:
- Provide colors and fonts as design tokens (.json or .scss).
- Ready to apply in Flutter and TailwindCSS environments.
---

## Prompt 10: UAE PASS Integration for SOCMINT Authentication

Integrate UAE PASS as the primary identity provider (IdP) into the SOCMINT SaaS platform for secure authentication and digital signature support.

### Backend (FastAPI)

Create a new service or module named `auth_uaepass` inside `backend/auth_service/` that:

- Implements OAuth2 Authorization Code Flow with PKCE.
- Connects to UAE PASS sandbox endpoints:
  - Authorization URL
  - Token URL
  - Userinfo endpoint
- Verifies ID token via OpenID Connect.
- Extracts national_id, full_name, phone, email.
- Maps user to internal SOCMINT tenant/user/role.
- Issues SOCMINT JWT including tenant_id, role, permissions.

### API Endpoints

- `GET /auth/uaepass/login` — UAE PASS redirect.
- `GET /auth/uaepass/callback` — Token exchange and user mapping.
- `GET /auth/profile` — Current session data.
- `POST /auth/logout` — Terminate session.

### Configuration (.env)

- `UAE_PASS_CLIENT_ID=...`
- `UAE_PASS_CLIENT_SECRET=...`
- `UAE_PASS_AUTH_URL=https://stg-id.uaepass.ae/idshub/authorize`
- `UAE_PASS_TOKEN_URL=https://stg-id.uaepass.ae/idshub/token`
- `UAE_PASS_USERINFO_URL=https://stg-id.uaepass.ae/idshub/userinfo`
- `REDIRECT_URI=https://socmint.ae/auth/uaepass/callback`

### Frontend (Flutter)

- Button: "تسجيل الدخول عبر الهوية الرقمية".
- Redirect to `/auth/uaepass/login`.
- Store returned JWT securely.
- Display current user from `/auth/profile`.
- Route to dashboard based on role (admin, analyst, viewer).

### Security

- Use HTTPS for all interactions.
- Validate JWT using UAE PASS JWKs.
- Implement refresh/expiration logic as needed.

### Output

- Working end-to-end login using UAE PASS.
- Internal SOCMINT role assignment per user.
- Secure session with JWT and Flutter state binding.
---

## Prompt 1: SOCMINT Infrastructure with Docker Compose

Design a scalable, modular infrastructure for the SOCMINT SaaS platform using Docker Compose.

### Objective

Deploy a full backend infrastructure using microservices to support OSINT ingestion, AI analytics, financial crime detection, and forensic investigations. Ensure each component runs in an isolated container and communicates over a secure Docker network.

### Services to Include

1. **Elasticsearch**
   - Port: 9200
   - Cluster config via environment variables
   - Persistent volume: `esdata`

2. **PostgreSQL**
   - Port: 5432
   - Credentials: `user=socmint`, `password=securepassword`, `db=socmint_db`
   - Volume: `pgdata`

3. **Neo4j**
   - Ports: 7474 (HTTP), 7687 (Bolt)
   - Default credentials
   - Volume: `neo4jdata`

4. **Apache Kafka + Zookeeper**
   - Kafka port: 9092
   - Zookeeper port: 2181
   - Network alias: `kafka`

5. **Apache Spark (Standalone)**
   - Port: 8080
   - Include master and worker nodes if needed

6. **FastAPI Backend (Microservice Ready)**
   - Folder: `./backend/`
   - Port: 8000
   - Built with Python 3.10+, uvicorn

7. **Frontend Web (Placeholder)**
   - Folder: `./frontend/`
   - Port: 80
   - Served via nginx or Flutter in later steps

8. **TOR Proxy**
   - Port: 9050
   - Expose SOCKS5 proxy for dark web scraping

9. **Docker Network**
   - All services should be attached to `socmint_network`

### Folder Structure

```
socmint-platform/
├── docker-compose.yml
├── backend/
├── frontend/
├── tor/
│   └── Dockerfile
├── .env
└── README.md
```

### docker-compose.yml Expectations

- All services configured with:
  - restart policy
  - named volumes
  - environment variables from `.env`
  - network alias
- Only backend and frontend exposed to the host
- Logging and healthchecks optional but recommended

### Output

- Fully functional `docker-compose.yml`
- Dockerfiles (for tor, backend, and optionally frontend)
- Sample `.env` with secure values
- `README.md` with build and run instructions
---

## Prompt 2: OSINT Data Collector Microservice (Social APIs + Web Scraping + TOR)

Design a FastAPI microservice named `data_collector` to ingest and normalize data from multiple open-source intelligence (OSINT) sources.

### Objective

Collect structured and unstructured data from social media APIs and websites, including content from the dark web using a TOR proxy, and push the results into Kafka for further processing.

### Microservice Structure

backend/
└── data_collector/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── collectors/
    │   ├── facebook_collector.py
    │   ├── twitter_collector.py
    │   ├── reddit_collector.py
    │   ├── instagram_collector.py
    │   ├── whatsapp_collector.py
    ├── scraper/
    │   ├── regular_scraper.py
    │   └── darkweb_scraper.py
    └── utils/
        └── helpers.py

### Functional Requirements

1. **API Collectors**
   - Use OAuth2 or token auth.
   - Fetch latest posts/comments/messages.
   - Normalize results (text, author, timestamp, source).
   - Push to Kafka topic: `raw_social_data`.

2. **Web Scraping Modules**
   - `regular_scraper.py`: For surface web scraping using Scrapy or Selenium.
   - `darkweb_scraper.py`: Uses TOR SOCKS5 proxy at `localhost:9050`.
   - Output to Kafka topic: `raw_scraped_data`.

3. **FastAPI Endpoints**
   - `POST /collect/<platform>` — Triggers API collection (e.g., facebook, twitter).
   - `POST /scrape` — Generic web scraping job.
   - `POST /scrape/darkweb` — Triggers dark web scraping via TOR.
   - `GET /status` — Returns health status of scrapers and API connectivity.

### Dockerfile Requirements

- Python 3.10+
- Packages: fastapi, uvicorn, requests, scrapy, selenium, kafka-python, torpy, python-dotenv
- Include Chrome and ChromeDriver for headless scraping

### .env Configuration

- `KAFKA_BROKER=kafka:9092`
- `TOR_PROXY=socks5h://localhost:9050`
- Social media tokens and API keys

### Kafka Topics

- `raw_social_data`: All social API output
- `raw_scraped_data`: All scraped content (including dark web)

### Output

- Full Dockerized microservice
- Modular collectors and scrapers
- Kafka integration with retry logic
- API with secure environment variables and status health check
---

## Prompt 3: AI Analytics Microservice (NLP + Classification)

Develop a FastAPI microservice named `ai_analytics_service` that analyzes textual data using NLP and AI models to generate actionable insights.

### Objective

Consume raw social and scraped data from Kafka, process it using machine learning models (sentiment, NER, topic classification), and output results to Elasticsearch and Neo4j.

### Microservice Structure

backend/
└── ai_analytics_service/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── models/
    │   ├── sentiment_analysis.py
    │   ├── ner.py
    │   └── topic_classification.py
    └── utils/
        ├── kafka_consumer.py
        ├── elasticsearch_client.py
        └── neo4j_client.py

### Functional Requirements

1. **Kafka Integration**
   - Consume messages from:
     - `raw_social_data`
     - `raw_scraped_data`
   - Batch or streaming mode

2. **Text Processing**
   - Sentiment Analysis using AraBERT/mBERT
   - Named Entity Recognition (NER): extract Person, Location, Org
   - Topic Classification (e.g. crime, politics, finance)

3. **Data Output**
   - Write enriched data to Elasticsearch index `processed_data`
   - Create entity graphs and relationships in Neo4j

4. **API Endpoints**
   - `GET /health`
   - `POST /test` — Accepts text and returns sentiment/NER/topic result
   - `GET /models` — Lists available NLP models

### Output Format

```json
{
  "source": "twitter",
  "text": "...",
  "sentiment": { "label": "negative", "confidence": 0.91 },
  "entities": [
    {"type": "PERSON", "value": "John Doe"},
    {"type": "ORG", "value": "Interpol"}
  ],
  "topic": "cybercrime",
  "timestamp": "2025-05-07T10:00:00Z"
}
```

### Dockerfile & Env

- Python 3.10+, torch, transformers, elasticsearch, neo4j-driver, kafka-python
- `.env` includes Kafka brokers, Elasticsearch/Neo4j URIs, model paths

### Output

- Kafka-to-AI pipeline with real-time text analytics
- NLP-processed results into Elasticsearch
- Graph data written to Neo4j
- Docker-ready service with clean FastAPI interface
---

## Prompt 4: Financial Crime Detection Microservice

Create a FastAPI microservice named `financial_crime_service` to identify financial crimes such as money laundering or fraud using machine learning.

### Objective

Analyze structured and unstructured financial behavior using clustering and anomaly detection algorithms. Visualize and store findings in PostgreSQL and Neo4j.

### Microservice Structure

backend/
└── financial_crime_service/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── analytics/
    │   ├── anomaly_detection.py
    │   ├── clustering.py
    │   └── graph_risk_analysis.py
    └── utils/
        ├── elasticsearch_connector.py
        ├── postgres_connector.py
        └── neo4j_connector.py

### Functional Requirements

1. **Anomaly Detection**
   - Use Isolation Forest to detect unusual patterns
   - Flag risky entities or transactions

2. **Clustering**
   - Apply KMeans to group entities by behavior
   - Identify fraud rings or money routes

3. **Graph Analysis**
   - Push relationships to Neo4j
   - Use PageRank or Betweenness Centrality

4. **API Endpoints**
   - `POST /run-analysis` — Full detection flow
   - `GET /alerts` — Recent risk flags
   - `GET /clusters` — Groupings of risky entities

5. **PostgreSQL Schema**
   - `financial_alerts(id, tenant_id, entity, score, reason, timestamp)`
   - `clusters(cluster_id, member_id, risk_level)`

6. **Neo4j Graph Schema**
   - Nodes: Person, Company, Account, Transaction
   - Relationships: `OWNS`, `TRANSFERRED_TO`, `SUSPICIOUS_LINKED`

### Dockerfile & Env

- Python 3.10+, pandas, scikit-learn, elasticsearch, psycopg2-binary, neo4j-driver
- `.env` includes DB creds, ES/Neo4j endpoints

### Output

- Anomaly flags into PostgreSQL
- Graph structure in Neo4j
- Clear REST API to view alerts and clusters
- Docker-ready service
---

## Prompt 5: Cyber Forensics & Blockchain Logging Microservice

Develop a FastAPI microservice named `cyber_forensics_service` to reconstruct incidents, correlate digital evidence, and log data integrity on blockchain.

### Objective

Support digital investigations by generating incident timelines, linking OSINT + logs + financial anomalies, and preserving evidence integrity using Ethereum or Hyperledger.

### Microservice Structure

backend/
└── cyber_forensics_service/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── forensics/
    │   ├── timeline_reconstruction.py
    │   ├── evidence_correlation.py
    │   └── blockchain_logger.py
    └── utils/
        ├── elasticsearch_fetcher.py
        ├── postgres_writer.py
        └── blockchain_client.py

### Functional Requirements

1. **Timeline Reconstruction**
   - Extract and sort logs from Elasticsearch index `security_logs`
   - Build chronological JSON timeline with actor, event, impact

2. **Evidence Correlation**
   - Match OSINT, financial data, and cyber logs into unified case file
   - Store full report in PostgreSQL

3. **Blockchain Logging**
   - Use Ethereum or Hyperledger to hash + timestamp each forensic report
   - Save hash, txID, and timestamp in `evidence_log`

4. **API Endpoints**
   - `POST /generate-report`
   - `GET /report/{id}`
   - `GET /verify/{id}`
   - `GET /health`

5. **PostgreSQL Schema**
   - `incident_reports(id, tenant_id, title, timeline_json, blockchain_tx, created_at)`
   - `evidence_log(id, report_id, sha256_hash, blockchain_reference, timestamp)`

### Blockchain (.env)

- `BLOCKCHAIN_PROVIDER=https://rpc-url`
- `PRIVATE_KEY=...`
- `CHAIN_ID=...`
- Optional smart contract integration

### Dockerfile & Env

- Python 3.10+, elasticsearch, psycopg2, web3.py, cryptography
- Securely mount blockchain keys and credentials

### Output

- Immutable forensic reports per incident
- API access for human and machine
- Blockchain-verified integrity
- Docker-compatible with full traceability
---

## Prompt 6: Flutter Web Frontend with UAE PASS, Multilingual Support & UAE Identity Design

Develop a Flutter Web application named `socmint_dashboard` with UAE government-compliant design, UAE PASS authentication, and multi-role dashboards.

### Objective

Deliver a responsive, secure frontend that connects to SOCMINT backend services via REST APIs, supports Arabic/English/Farsi/Russian, and provides a professional UAE-branded interface.

### Project Structure

frontend_flutter/
├── Dockerfile
├── nginx.conf
├── pubspec.yaml
├── lib/
│   ├── main.dart
│   ├── app.dart
│   ├── config/app_routes.dart
│   ├── services/api_service.dart
│   ├── services/auth_service.dart
│   ├── localization/
│   │   ├── intl_ar.arb
│   │   ├── intl_en.arb
│   │   ├── intl_fa.arb
│   │   └── intl_ru.arb
│   ├── screens/
│   │   ├── login.dart
│   │   ├── dashboard_admin.dart
│   │   ├── dashboard_analyst.dart
│   │   ├── dashboard_viewer.dart
│   │   └── data_source_manager.dart
│   └── widgets/
│       ├── navigation_drawer.dart
│       └── uae_button.dart

### Functional Requirements

1. **Authentication**
   - JWT login + role-based routing
   - Optional UAE PASS OAuth2 login
   - Store JWT securely (encrypted local storage)

2. **Multilingual Support**
   - RTL for Arabic & Farsi
   - LTR for English & Russian
   - Use `intl` and `flutter_localizations`

3. **Role-Specific Dashboards**
   - Admin: Manage sources, users, full access
   - Analyst: View analytics, alerts, reports
   - Viewer: Read-only insights & trends

4. **Design System**
   - UAE Design guidelines
   - Use Dubai/Noto Kufi fonts
   - Rounded buttons, dark sidebar, light/dark mode toggle

5. **API Integration**
   - Connect via Dio to:
     - `/auth`, `/analytics`, `/timeline`, `/posts`, `/alerts`, `/reports`
   - Token-based header injection and error handling

### Dockerfile & Deployment

- Base image: `cirruslabs/flutter:stable-web`
- Run: `flutter build web`
- Serve via nginx (port 80)

### Output

- Secure, responsive, multilingual Flutter frontend
- Role-based views tied to SOCMINT backend
- UAE PASS integration optional but ready
- Docker-ready frontend with full branding
---

## Prompt 7: Full Deployment, Integration & Testing of SOCMINT Platform

Deploy and validate the entire SOCMINT SaaS infrastructure using Docker Compose on an Ubuntu Server.

### Objective

Ensure all services (backend, frontend, data pipelines, AI models, storage layers, and integrations) function correctly and are production-ready.

---

### Environment Requirements

- Ubuntu Server 20.04+  
- Docker & Docker Compose installed  
- 16-core CPU, 32 GB RAM, 512 GB SSD  
- Internet access for pulling containers and UAE PASS sandbox testing

---

### Phase 1: Infrastructure Validation

1. **Start Services**

```bash
docker-compose up -d
```

2. **Verify Containers**

```bash
docker-compose ps
```

3. **Network Connectivity**

Ensure services communicate via `socmint_network`.

4. **Test Access via Curl or Browser**

| Service        | Port | Test Command                           |
|----------------|------|----------------------------------------|
| Frontend       | 80   | `curl http://localhost`                |
| Backend (API)  | 8000 | `curl http://localhost:8000/health`    |
| Elasticsearch  | 9200 | `curl http://localhost:9200/_cat/indices` |
| PostgreSQL     | 5432 | Connect using `psql`                   |
| Neo4j          | 7474 | Open browser and login                 |

---

### Phase 2: Kafka & Database Testing

1. **Kafka Topic Test**

```bash
docker exec -it kafka bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

2. **Test Message Production/Consumption**

Send a sample message to `raw_social_data` and ensure it's consumed by the AI service.

3. **PostgreSQL**

Ensure tables are created:

```sql
SELECT * FROM financial_alerts;
SELECT * FROM incident_reports;
```

---

### Phase 3: Backend API Testing

Use Postman or curl to test:

- `/collect/twitter`
- `/scrape/darkweb`
- `/run-analysis`
- `/generate-report`
- `/verify/<report_id>`
- `/auth/uaepass/login`

---

### Phase 4: Frontend Testing

1. **Test Role-Based Views**

- Login with Admin → verify access to all dashboards
- Login with Analyst → verify analytics only
- Login with Viewer → read-only view

2. **Test Language Switching**

- Switch to Arabic, Farsi, Russian and verify layout

3. **Test UAE PASS Integration**

- Redirect to sandbox login
- Verify JWT returned and user profile loaded

---

### Phase 5: TOR Validation

1. **Scraping through TOR**

Test dark web access via:

```bash
curl --socks5-hostname localhost:9050 http://check.torproject.org
```

Verify scraping via `/scrape/darkweb`.

---

### Phase 6: Final Review

- Logs: `docker-compose logs <service>`
- Resource Usage: `docker stats`
- Backup: Dump PostgreSQL and Elasticsearch data
- Security: Ensure HTTPS for public-facing services

---

### Output

- All services functional
- End-to-end data flow validated
- Frontend + backend + data layers + blockchain tested
- Platform ready for production deployment
---

## Prompt 8: Social Media Manager Microservice (Postiz Integration)

Integrate the open-source Postiz App as a multi-tenant social media management microservice within the SOCMINT platform.

### Objective

Enable each tenant to securely manage their social media accounts (Facebook, Twitter, LinkedIn, etc.) for scheduling, publishing, and analytics — isolated per customer.

---

### Microservice Structure

backend/
└── social_media_manager/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── routes/
    │   ├── auth.py
    │   ├── posts.py
    │   ├── scheduler.py
    │   └── analytics.py
    ├── models/
    │   ├── user.py
    │   ├── tenant.py
    │   ├── post.py
    │   └── campaign.py
    └── utils/
        ├── token_verification.py
        └── oauth_handler.py

---

### Functional Requirements

1. **Multi-Tenant Auth Integration**
   - Validate JWT from SOCMINT’s identity provider
   - Enforce tenant isolation via `tenant_id`

2. **Social Media API Integration**
   - OAuth2 integration for Twitter, Facebook, LinkedIn
   - Store tokens per tenant and refresh periodically

3. **Post Scheduling and Publishing**
   - Create and schedule posts
   - Trigger posting jobs with APScheduler or Celery
   - Monitor status (published, failed, queued)

4. **Analytics Reporting**
   - Track engagements (likes, comments, reach)
   - Generate per-campaign reports
   - Output to PostgreSQL and optionally Elasticsearch

5. **API Endpoints**
   - `POST /connect/account`
   - `POST /schedule`
   - `GET /posts`
   - `GET /analytics/campaign/{id}`

---

### PostgreSQL Schema

- `social_accounts(id, tenant_id, platform, token, refresh_token)`
- `posts(id, tenant_id, content, scheduled_time, status)`
- `campaigns(id, tenant_id, name, metrics_json)`

---

### Flutter Frontend Additions

- Add screen `SocialMediaManagerScreen`
- Features:
  - Account linking and status
  - Post calendar
  - Campaign insights

---

### Dockerfile

- Python 3.10+, FastAPI, APScheduler, OAuthlib, SQLAlchemy, psycopg2

---

### Security Considerations

- Use HTTPS
- Isolate all tenant data via `tenant_id`
- Encrypt API tokens at rest

---

### Output

- Fully working multi-tenant social media manager
- Postiz-based code adapted for SOCMINT
- Integrated into backend and visible in frontend
- Analytics tracked per tenant
---

## Prompt 9: Visual Identity System for SOCMINT by RHAL

Design a complete visual identity system for the SOCMINT platform under the branding of "RHAL – عجمان للتقنيات المتقدمة".

### Objective

Establish a consistent, professional identity across all user interfaces, dashboards, reports, and communications that reflects the sovereignty, intelligence, and UAE heritage of the product.

---

### Design Components

1. **Color Palette**
   - Primary: Extracted green tone from logo
   - Secondary: White, black, soft gray
   - Accent: Emirati flag red (alerts, errors)

2. **Typography**
   - Arabic: Dubai Font or Noto Kufi Arabic
   - English: Montserrat or Source Sans Pro
   - Consistent font weights for headings and body

3. **UI Elements**
   - Buttons: Rounded corners, green hover effect
   - Cards: Minimalist, light shadow, 12px radius
   - Sidebars: Dark background with active section highlight in green

4. **Logo Usage**
   - Always preserve the green bar above "رحّال"
   - Primary version: white on black
   - Maintain clear space equal to letter height around logo
   - No distortion, recoloring, or inversion

5. **Dashboard Layout**
   - Left sidebar for navigation
   - Top bar with logo and user menu
   - Main content: Grid for charts, KPIs, alerts
   - Default dark mode, with light mode toggle

6. **Landing Page Design**
   - Hero: centered logo + tagline ("منصة الاستخبارات السيادية متعددة القنوات")
   - Sections: About, Features, Dashboard, Subscribe
   - Language switch (ar/en) at top right

7. **Document Style Guide**
   - Logo variants (color, black/white, favicon)
   - Font hierarchy for titles, subtitles, body
   - Templates for PDF reports and presentations

8. **Icons and Favicon**
   - Create square icon version of the logo
   - Sizes: 512x512, 192x192, 48x48
   - Export SVG and PNG formats

---

### Implementation Notes

- Export color codes and fonts as Flutter ThemeData & Tailwind CSS variables
- All components must be RTL-ready and responsive
- Ensure consistency across Flutter, PDF exports, and external reports

---

### Output

- Design system documentation
- UI kit (color tokens, font stacks, component examples)
- Logo guidelines and assets
- Style guide for documents and landing pages
---

## Prompt 10: UAE PASS Integration for SOCMINT Authentication

Integrate UAE PASS as the primary identity provider (IdP) into the SOCMINT SaaS platform for secure authentication and digital identity validation.

### Objective

Allow SOCMINT users to authenticate via UAE PASS using OpenID Connect (OIDC), ensuring national identity-level assurance and regulatory compliance.

---

### Backend Configuration (FastAPI)

1. **Service Name:** `auth_uaepass`
2. **Authentication Flow:**
   - OAuth2 Authorization Code with PKCE
   - UAE PASS Sandbox endpoints:
     - `https://stg-id.uaepass.ae/idshub/authorize`
     - `https://stg-id.uaepass.ae/idshub/token`
     - `https://stg-id.uaepass.ae/idshub/userinfo`

3. **Functionality:**
   - Redirect user to UAE PASS login
   - Handle authorization code callback
   - Exchange token
   - Retrieve user info and extract:
     - Emirates ID
     - Full name
     - Mobile number
     - Email
   - Map UAE PASS user to internal `tenant_id`, `user_id`, and `role`
   - Issue SOCMINT JWT token

4. **Endpoints:**
   - `GET /auth/uaepass/login`
   - `GET /auth/uaepass/callback`
   - `GET /auth/profile`
   - `POST /auth/logout`

---

### .env Variables

```env
UAE_PASS_CLIENT_ID=...
UAE_PASS_CLIENT_SECRET=...
UAE_PASS_AUTH_URL=https://stg-id.uaepass.ae/idshub/authorize
UAE_PASS_TOKEN_URL=https://stg-id.uaepass.ae/idshub/token
UAE_PASS_USERINFO_URL=https://stg-id.uaepass.ae/idshub/userinfo
REDIRECT_URI=https://socmint.ae/auth/uaepass/callback
```

---

### Frontend Integration (Flutter)

1. Add login option "تسجيل الدخول عبر الهوية الرقمية"
2. On click:
   - Redirect to `/auth/uaepass/login`
3. On success:
   - Receive JWT and store securely
   - Route to user dashboard based on role
   - Display name/national ID in profile

---

### Security Considerations

- All tokens via HTTPS
- Validate JWTs with UAE PASS public keys
- Verify nonce, audience, and expiration
- Log all login attempts and token transactions

---

### Output

- End-to-end authentication flow via UAE PASS
- JWT mapped to SOCMINT roles and tenants
- Secure and verifiable login
- Fully integrated backend + Flutter support
