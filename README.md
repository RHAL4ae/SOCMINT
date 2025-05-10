# SOCMINT Developer README 🧠💻

This technical README provides a comprehensive overview of the SOCMINT platform from a development and deployment perspective. It includes setup instructions, architectural layout, services, APIs, and integration flows.

---

## 🧱 System Architecture

SOCMINT is a multi-service SaaS platform composed of:

- **Frontend**: Vue.js + Tailwind + i18n + UAE PASS OAuth
- **Backend**: FastAPI microservices
- **Data Layer**: PostgreSQL + Elasticsearch + Neo4j
- **AI & Processing**: Kafka, Python ML services, LangChain, HuggingFace, DeepSeek
- **Security & Identity**: JWT, UAE PASS OAuth2.0, Blockchain logging, TOR routing

---

## 🔧 Tech Stack

| Component       | Stack                         |
|----------------|-------------------------------|
| Frontend        | Vue 3, Pinia, Vue Router, Tailwind |
| Backend         | FastAPI, LangChain, Pydantic, Redis |
| AI Services     | HuggingFace Transformers, DeepSeek R1, Google NLP |
| Databases       | PostgreSQL, Elasticsearch, Neo4j |
| Messaging       | Kafka (for social + media ingestion) |
| Identity/Auth   | UAE PASS OAuth, JWT            |
| Scraping Layer  | Playwright, Selenium, cURL-TOR |
| Deployment      | Docker Compose, Traefik, .env |

---

## 🚀 Deployment Instructions

1. Clone the repo:
```bash
git clone https://github.com/rhal4ae/SOCMINT.git
cd SOCMINT
```

2. Create environment variables:
```bash
cp .env.example .env
```

3. Launch with Docker Compose:
```bash
docker-compose up -d
```

4. Access:
- Frontend: `http://localhost`
- Backend: `http://localhost:8000`
- Elasticsearch: `http://localhost:9200`
- Neo4j: `http://localhost:7474`

---

## 📡 API Endpoints

| Endpoint                   | Method | Description                        |
|---------------------------|--------|------------------------------------|
| /auth/uaepass/login       | GET    | Redirects to UAE PASS              |
| /collect/twitter          | POST   | Pull Twitter/X data                |
| /scrape/darkweb           | GET    | Scrape dark web posts              |
| /run-analysis             | POST   | Run NLP/ML models                  |
| /generate-report          | GET    | Generate intelligence report       |
| /verify/<report_id>       | GET    | Validate + audit report            |
| /api/media/alerts         | GET    | Return sentiment alerts            |

---

## 🧪 Testing & Validation

Use Postman or `curl` to test APIs.  
Validate role-based access (Admin, Analyst, Viewer).  
Enable UAE PASS sandbox login for SSO test.  
Use TOR for dark web scraping:

```bash
curl --socks5-hostname localhost:9050 http://check.torproject.org
```

---

## 📊 KPIs & Analytics

- Integrated with GEM 2.1 indicators
- Stored in Elasticsearch (index: `kpi_metrics_monthly`)
- Displayed in `RahhalKPI.vue` dashboard

---

## 🌐 Integrated Platforms

- Facebook Graph API
- Twitter/X API v2
- Telegram Bot API
- WhatsApp Business Cloud API
- TikTok + Snap Map via Web Scraping
- Google Business Profile API
- Reddit JSON endpoints
- Dark Web (via TOR scraping)

---

## 🛡️ Security Considerations

- HTTPS via Traefik
- Blockchain logging of report trails
- Verifiable credentials via DID
- TOR routing via dockerized SOCKS5
- JWT session enforcement

---

## 📁 File Structure (Simplified)

```
SOCMINT/
│
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── services/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── views/
│
├── docker-compose.yml
├── .env.example
├── nginx/ + traefik/
```

---

## 🧠 AI Agents

Supports modular LLM agents for:
- Entity classification
- Financial anomaly detection
- Risk scoring via DeepSeek R1
- NLP-based media profiling

---

## 🤝 Contribution Guidelines

- Use clear commit messages
- Document API changes
- Follow PEP8 / ESLint standards
- Add prompt-based AI test coverage
- Maintain `.env.example` always

---

## Maintained by

Rami Kamel | SOCMINT Architect  
Ajman, UAE 🇦🇪 | AI + Cybersecurity Fellow  
# SOCMINT – منصة الاستخبارات السيادية متعددة القنوات

## المقدمة  
SOCMINT هي منصة SaaS متكاملة لجمع وتحليل المعلومات المفتوحة (OSINT)، ومراقبة وسائل التواصل الاجتماعي، واكتشاف الجرائم المالية، والتحقيق الجنائي الرقمي، مدعومة بأحدث نماذج الذكاء الاصطناعي وقابلية النشر السريعة عبر الحاويات. تهدف المنصة إلى مساعدة المحققين وأخصائيي الأمن في الحصول على رؤى فورية من بيانات متنوعة وموزعة عبر واجهة موحدة ومؤمَّنة.

---

## المتطلبات البيئية  
- **نظام التشغيل**: Ubuntu Server 20.04+ أو ما يعادله  
- **حاويات**: Docker ≥20.10, Docker Compose ≥1.29  
- **موارد النظام**: CPU 16-core, RAM 32 GB, SSD 512 GB  
- **شبكة**: اتصال داخلي آمن لـ Kafka, Elasticsearch, Neo4j, PostgreSQL  
- **أدوات تطوير**: Python 3.10+, Flutter SDK (للواجهة), Node.js (إذا لزم)

---

## الهيكلية العامة للمشروع  
```
socmint-platform/
├── backend/
│   ├── data_collector/            # جمع البيانات (OSINT + Web Scraping)
│   ├── ai_analytics_service/      # معالجة النصوص (NLP + تصنيف)
│   ├── financial_crime_service/   # اكتشاف الجرائم المالية (Anomaly & Clustering)
│   ├── cyber_forensics_service/   # التحقيق الجنائي وتوثيق البلوكتشين
│   ├── social_media_manager/      # إدارة ونشر المحتوى عبر Postiz
│   └── auth_uaepass/              # تكامل UAE PASS (OIDC)
├── frontend_flutter/              # لوحة التحكم (Flutter Web)
├── tor/                           # إعداد TOR Proxy  
│   └── Dockerfile  
├── docker-compose.yml             # تنسيق تشغيل جميع الخدمات  
├── .env                           # متغيرات البيئة المشتركة  
└── README.md                      # هذا الملف  
```

---

## تفاصيل الخدمات المصغرة (Microservices)

### 1. data_collector  
- **وصف**: يجمع البيانات من APIs لوسائل التواصل (Facebook, Twitter, Reddit, Instagram, WhatsApp) ويجري Web Scraping، بما في ذلك ويب الظلام عبر TOR  
- **نقاط النهاية**:  
  - `POST /collect/<platform>`  
  - `POST /scrape`  
  - `POST /scrape/darkweb`  
  - `GET /status`  
- **المخرجات**: تُدفع الرسائل إلى Kafka Topics: `raw_social_data` و `raw_scraped_data`  

### 2. ai_analytics_service  
- **وصف**: يستهلك بيانات Kafka ويطبّق نماذج AraBERT/mBERT لتحليل المشاعر، واستخراج الكيانات، وتصنيف المواضيع، ثم يكتب النتائج إلى Elasticsearch و Neo4j  
- **نقاط النهاية**:  
  - `GET /health`  
  - `POST /test`  
  - `GET /models`  
- **مخرجات**: Elasticsearch index `processed_data`، ورسومات الكيانات في Neo4j  

### 3. financial_crime_service  
- **وصف**: يستخدم Isolation Forest و KMeans لاكتشاف الأنماط غير المعتادة وتكوين مجموعات الكيانات المشبوهة، مع دفع النتائج إلى PostgreSQL و Neo4j  
- **نقاط النهاية**:  
  - `POST /run-analysis`  
  - `GET /alerts`  
  - `GET /clusters`  

### 4. cyber_forensics_service  
- **وصف**: يعيد بناء جداول زمنية للحوادث من Elasticsearch، يربط الأدلة الرقمية مع البيانات المالية، ويوثق سلامة التقارير عبر البلوكتشين (Ethereum/Hyperledger)  
- **نقاط النهاية**:  
  - `POST /generate-report`  
  - `GET /report/{id}`  
  - `GET /verify/{id}`  
  - `GET /health`  

### 5. social_media_manager  
- **وصف**: يدمج Postiz App لتمكين كل مستأجر من جدولة ونشر المحتوى وقياس التفاعل بشكل معزول  
- **نقاط النهاية**:  
  - `POST /connect/account`  
  - `POST /schedule`  
  - `GET /posts`  
  - `GET /analytics/campaign/{id}`  

### 6. auth_uaepass  
- **وصف**: يحقن تدفق OAuth2 Authorization Code مع PKCE عبر UAE PASS Sandbox لتوثيق المستخدمين بمستوى الثقة الوطني  
- **نقاط النهاية**:  
  - `GET /auth/uaepass/login`  
  - `GET /auth/uaepass/callback`  
  - `GET /auth/profile`  
  - `POST /auth/logout`  

---

## واجهة المستخدم – socmint_dashboard (Flutter)  
- **الميزات**:  
  - دعم RTL/LTR لأربع لغات (عربي، إنجليزي، فارسي، روسي)  
  - تسجيل دخول قياسي وجزئي عبر UAE PASS  
  - لوحات دورية (Admin, Analyst, Viewer)  
- **البنية**:  
  - `lib/screens/`  
  - `lib/services/`  
  - `lib/localization/intl_*.arb`  

---

## docker-compose.yml  
```yaml
version: '3.8'
services:
  kafka:
    image: bitnami/kafka:latest
    ports: ['9092:9092']
    # إعدادات Zookeeper و env...
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.0
    ports: ['9200:9200']
    volumes: ['esdata:/usr/share/elasticsearch/data']
  postgres:
    image: postgres:13
    ports: ['5432:5432']
    environment:
      POSTGRES_USER: socmint
      POSTGRES_PASSWORD: securepassword
      POSTGRES_DB: socmint_db
    volumes: ['pgdata:/var/lib/postgresql/data']
  neo4j:
    image: neo4j:4.4
    ports: ['7474:7474','7687:7687']
    volumes: ['neo4jdata:/data']
  tor:
    build: ./tor
    ports: ['9050:9050']
  backend_data_collector:
    build: ./backend/data_collector
    depends_on: ['kafka','tor']
  backend_ai_analytics:
    build: ./backend/ai_analytics_service
    depends_on: ['kafka','elasticsearch','neo4j']
  backend_financial_crime:
    build: ./backend/financial_crime_service
    depends_on: ['postgres','neo4j']
  backend_cyber_forensics:
    build: ./backend/cyber_forensics_service
    depends_on: ['elasticsearch','postgres']
  backend_social_manager:
    build: ./backend/social_media_manager
    depends_on: ['postgres']
  backend_auth:
    build: ./backend/auth_uaepass
    depends_on: ['postgres']
  frontend:
    build: ./frontend_flutter
    ports: ['80:80']
volumes:
  esdata: {}
  pgdata: {}
  neo4jdata: {}
networks:
  default:
    name: socmint_network
```

---

## ملف المتغيرات البيئة (.env)  
```
# Kafka
KAFKA_BROKER=kafka:9092

# TOR
TOR_PROXY=socks5h://tor:9050

# PostgreSQL
POSTGRES_USER=socmint
POSTGRES_PASSWORD=securepassword
POSTGRES_DB=socmint_db
POSTGRES_HOST=postgres

# Elasticsearch & Neo4j
ELASTICSEARCH_URL=http://elasticsearch:9200
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=neo4j

# UAE PASS
UAE_PASS_CLIENT_ID=…
UAE_PASS_CLIENT_SECRET=…
UAE_PASS_AUTH_URL=https://stg-id.uaepass.ae/idshub/authorize
UAE_PASS_TOKEN_URL=https://stg-id.uaepass.ae/idshub/token
UAE_PASS_USERINFO_URL=https://stg-id.uaepass.ae/idshub/userinfo
REDIRECT_URI=https://your-domain.com/auth/uaepass/callback
```

---

## خطوات التشغيل  
1. **الاستنساخ**  
   ```bash
   git clone https://github.com/RHAL4ae/SOCMINT.git
   cd SOCMINT
   ```  
2. **تكوين .env** كما هو موضح أعلاه.  
3. **بناء الحاويات وتشغيلها**  
   ```bash
   docker-compose up --build -d
   ```  
4. **التحقق**  
   - `curl http://localhost:8000/health`  
   - `curl http://localhost`  
   - `docker-compose logs -f`  

---

## استراتيجية الاختبار  
- **Kafka & قواعد البيانات**: تحقق من وجود Topics والجداول  
- **Backend APIs**: استخدم Postman أو curl لاختبار جميع نقاط النهاية  
- **واجهة Flutter**: تسجيل الدخول، تبديل اللغات، أدوار المستخدم  
- **TOR**:  
  ```bash
  curl --socks5-hostname localhost:9050 http://check.torproject.org
  ```  
- **التكامل النهائي**:  
  - توليد تقرير جنائي  
  - تحليل نصي  
  - اكتشاف جريمة مالية  
  - جدولة منشور ونشره  

---

## النشر وCI/CD  
- ادماج مع GitHub Actions أو GitLab CI لخطوات: lint, test, build, deploy  
- نشر إلى بيئة Kubernetes أو Docker Swarm عند الحاجة  
- ربط SSL و Load Balancer  

---

## التوصيات الأمنية  
- إجبار HTTPS لجميع الخدمات  
- تشفير متغيرات البيئة الحساسة  
- إدارة مفاتيح البلوكتشين في Secret Manager  
- جدران حماية داخلية لعزل الحاويات  
- مراقبة السجلات وتنبيهات SIEM  

---

## المساهمة  
1. فتح Issue لوصف الميزة أو العطل.  
2. إنشاء فرع جديد `feature/…` أو `bugfix/…`.  
3. تقديم Pull Request مع الوصف والاختبارات.  
4. الانتظار للمراجعة والدمج.  

---

> _هذا المستند يهدف إلى توجيه المطورين لبدء العمل الفوري على منصة SOCMINT بكل تفاصيلها التقنية والمعمارية._# SOCMINT Implementation Prompts + General Guidelines

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
# OSINT Data Collector Microservice

## Overview

The OSINT Data Collector is a FastAPI microservice designed to ingest and normalize data from multiple open-source intelligence (OSINT) sources. It collects structured and unstructured data from social media APIs and websites, including content from the dark web using a TOR proxy, and pushes the results into Kafka for further processing.

## Features

- **Social Media API Integration**: Collect data from Facebook, Twitter, Reddit, Instagram, and WhatsApp using OAuth2 or token authentication
- **Web Scraping**: Surface web scraping using Scrapy or Selenium
- **Dark Web Access**: TOR integration for accessing .onion sites and other dark web content
- **Kafka Integration**: Normalized data streaming with retry logic
- **Modular Architecture**: Easily extendable for additional data sources
- **Containerized**: Fully Dockerized for easy deployment

## Architecture

```
data_collector/
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
```

## Setup

### Prerequisites

- Python 3.10+
- Docker
- Kafka instance
- TOR service (for dark web scraping)
- API keys for social media platforms

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```
# Kafka Configuration
KAFKA_BROKER=kafka:9092

# TOR Configuration
TOR_PROXY=socks5h://localhost:9050

# Facebook API
FACEBOOK_APP_ID=your_app_id
FACEBOOK_APP_SECRET=your_app_secret
FACEBOOK_ACCESS_TOKEN=your_access_token

# Twitter API
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_BEARER_TOKEN=your_bearer_token

# Reddit API
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
REDDIT_USER_AGENT=OSINT Data Collector v1.0

# Instagram API
INSTAGRAM_ACCESS_TOKEN=your_access_token

# WhatsApp API
WHATSAPP_API_KEY=your_api_key
```

### Installation

#### Using Docker

```bash
# Build the Docker image
docker build -t osint-data-collector .

# Run the container
docker run -d -p 8000:8000 --name osint-collector osint-data-collector
```

#### Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the service
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### Root
- `GET /` - Check if the API is running

### Status
- `GET /status` - Get the health status of all collectors, scrapers, and connections

### Social Media Collection
- `POST /collect/{platform}` - Trigger data collection from a specific social media platform
  - Supported platforms: facebook, twitter, reddit, instagram, whatsapp
  - Request body: JSON with query parameters specific to the platform

### Web Scraping
- `POST /scrape` - Trigger web scraping job for regular websites
  - Request body: JSON with scraping parameters

### Dark Web Scraping
- `POST /scrape/darkweb` - Trigger web scraping job for dark web sites via TOR
  - Request body: JSON with scraping parameters

## Usage Examples

### Collecting Facebook Posts

```bash
curl -X POST "http://localhost:8000/collect/facebook" \
  -H "Content-Type: application/json" \
  -d '{"page_id": "meta", "limit": 10}'
```

### Collecting Twitter Tweets

```bash
curl -X POST "http://localhost:8000/collect/twitter" \
  -H "Content-Type: application/json" \
  -d '{"query": "#osint", "max_results": 25}'
```

### Scraping a Website

```bash
curl -X POST "http://localhost:8000/scrape" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "method": "selenium",
    "selectors": {
      "headlines": "h1, h2, h3",
      "paragraphs": "p"
    }
  }'
```

### Scraping a Dark Web Site

```bash
curl -X POST "http://localhost:8000/scrape/darkweb" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://example.onion",
    "method": "requests",
    "timeout": 120
  }'
```

## Kafka Topics

- `raw_social_data`: All social API output
- `raw_scraped_data`: All scraped content (including dark web)

## Security Considerations

- All API keys and tokens are stored in environment variables
- TOR connection is used for dark web access
- OAuth2 or token authentication for social media APIs

## Error Handling

The service includes comprehensive error handling and retry logic:

- Kafka connection retries with exponential backoff
- TOR connection verification before dark web scraping
- API connection status checks

---

# خدمة جمع بيانات OSINT المصغرة

## نظرة عامة

جامع بيانات OSINT هو خدمة مصغرة مبنية على FastAPI مصممة لاستيعاب وتطبيع البيانات من مصادر متعددة للمعلومات الاستخباراتية مفتوحة المصدر (OSINT). تقوم بجمع البيانات المنظمة وغير المنظمة من واجهات برمجة تطبيقات وسائل التواصل الاجتماعي والمواقع الإلكترونية، بما في ذلك المحتوى من الويب المظلم باستخدام وكيل TOR، وتدفع النتائج إلى Kafka لمزيد من المعالجة.

## الميزات

- **تكامل واجهة برمجة تطبيقات وسائل التواصل الاجتماعي**: جمع البيانات من فيسبوك وتويتر وريديت وإنستغرام وواتساب باستخدام مصادقة OAuth2 أو الرمز المميز
- **كشط الويب**: كشط الويب السطحي باستخدام Scrapy أو Selenium
- **الوصول إلى الويب المظلم**: تكامل TOR للوصول إلى مواقع .onion ومحتوى الويب المظلم الآخر
- **تكامل Kafka**: تدفق البيانات المطبعة مع منطق إعادة المحاولة
- **هندسة معيارية**: قابلة للتوسيع بسهولة لمصادر بيانات إضافية
- **حاويات**: مُحوَّلة بالكامل إلى Docker لسهولة النشر

## الإعداد

### المتطلبات المسبقة

- Python 3.10+
- Docker
- مثيل Kafka
- خدمة TOR (لكشط الويب المظلم)
- مفاتيح API لمنصات وسائل التواصل الاجتماعي

### متغيرات البيئة

قم بإنشاء ملف `.env` في الدليل الجذر بالمتغيرات التالية:

```
# تكوين Kafka
KAFKA_BROKER=kafka:9092

# تكوين TOR
TOR_PROXY=socks5h://localhost:9050

# واجهة برمجة تطبيقات فيسبوك
FACEBOOK_APP_ID=your_app_id
FACEBOOK_APP_SECRET=your_app_secret
FACEBOOK_ACCESS_TOKEN=your_access_token

# واجهة برمجة تطبيقات تويتر
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_BEARER_TOKEN=your_bearer_token

# واجهة برمجة تطبيقات ريديت
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
REDDIT_USER_AGENT=OSINT Data Collector v1.0

# واجهة برمجة تطبيقات إنستغرام
INSTAGRAM_ACCESS_TOKEN=your_access_token

# واجهة برمجة تطبيقات واتساب
WHATSAPP_API_KEY=your_api_key
```

## نقاط النهاية API

### الجذر
- `GET /` - تحقق مما إذا كانت واجهة برمجة التطبيقات قيد التشغيل

### الحالة
- `GET /status` - الحصول على حالة صحة جميع المجمعين والكاشطات والاتصالات

### جمع وسائل التواصل الاجتماعي
- `POST /collect/{platform}` - تشغيل جمع البيانات من منصة وسائط اجتماعية محددة
  - المنصات المدعومة: facebook، twitter، reddit، instagram، whatsapp
  - نص الطلب: JSON مع معلمات الاستعلام الخاصة بالمنصة

### كشط الويب
- `POST /scrape` - تشغيل مهمة كشط الويب للمواقع العادية
  - نص الطلب: JSON مع معلمات الكشط

### كشط الويب المظلم
- `POST /scrape/darkweb` - تشغيل مهمة كشط الويب لمواقع الويب المظلم عبر TOR
  - نص الطلب: JSON مع معلمات الكشط

## اعتبارات الأمان

- يتم تخزين جميع مفاتيح API والرموز المميزة في متغيرات البيئة
- يتم استخدام اتصال TOR للوصول إلى الويب المظلم
- مصادقة OAuth2 أو الرمز المميز لواجهات برمجة تطبيقات وسائل التواصل الاجتماعي

## معالجة الأخطاء

تتضمن الخدمة معالجة شاملة للأخطاء ومنطق إعادة المحاولة:

- إعادة محاولات اتصال Kafka مع تراجع أسي
- التحقق من اتصال TOR قبل كشط الويب المظلم
- فحوصات حالة اتصال API


# AI Analytics Microservice

_English Documentation_

## Overview

The AI Analytics Microservice is a FastAPI-based service that analyzes textual data using NLP and AI models to generate actionable insights. It consumes raw social and scraped data from Kafka, processes it using machine learning models for sentiment analysis, named entity recognition (NER), and topic classification, and outputs the results to Elasticsearch and Neo4j.

## Features

- **Multilingual Support**: Processes both Arabic and English text using AraBERT/mBERT models
- **Sentiment Analysis**: Determines the sentiment of text (positive, negative, neutral)
- **Named Entity Recognition**: Extracts entities like Person, Location, and Organization
- **Topic Classification**: Categorizes text into topics like cybercrime, terrorism, financial crime, etc.
- **Kafka Integration**: Consumes messages from `raw_social_data` and `raw_scraped_data` topics
- **Data Output**: Writes enriched data to Elasticsearch and creates entity graphs in Neo4j

## Installation

### Prerequisites

- Python 3.8+
- Kafka
- Elasticsearch
- Neo4j

### Setup

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set environment variables (or create a `.env` file):

```
# Kafka
KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# Elasticsearch
ELASTICSEARCH_HOSTS=localhost:9200
ELASTICSEARCH_USERNAME=elastic
ELASTICSEARCH_PASSWORD=changeme

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=test

# NLP Models
SENTIMENT_MODEL=asafaya/bert-base-arabic-sentiment
NER_MODEL=aubmindlab/bert-base-arabertv02-ner
TOPIC_MODEL=facebook/bart-large-mnli
```

## Usage

### Running the Service

```bash
uvicorn main:app --reload
```

The service will be available at http://localhost:8000

### API Endpoints

- `GET /health` - Health check endpoint
- `POST /test` - Test endpoint to analyze a single text input
- `GET /models` - Lists available NLP models
- `POST /start-processing` - Start processing messages from Kafka
- `POST /stop-processing` - Stop processing messages from Kafka
- `GET /processing-status` - Get the current status of Kafka processing

### Example Request

```bash
curl -X POST "http://localhost:8000/test" \
     -H "Content-Type: application/json" \
     -d '{"text":"The cybercriminal stole data from Interpol headquarters in Lyon, France.", "source":"news"}'
```

### Example Response

```json
{
  "source": "news",
  "text": "The cybercriminal stole data from Interpol headquarters in Lyon, France.",
  "sentiment": { 
    "label": "negative", 
    "confidence": 0.91 
  },
  "entities": [
    {"type": "PERSON", "value": "cybercriminal"},
    {"type": "ORGANIZATION", "value": "Interpol"},
    {"type": "LOCATION", "value": "Lyon"},
    {"type": "LOCATION", "value": "France"}
  ],
  "topic": "cybercrime",
  "timestamp": "2025-05-07T10:00:00Z"
}
```

## Docker

Build and run the Docker container:

```bash
docker build -t ai_analytics_service .
docker run -p 8000:8000 ai_analytics_service
```

## Architecture

```
┌─────────────┐    ┌─────────────────────┐    ┌───────────────┐
│   Kafka     │───▶│  AI Analytics       │───▶│ Elasticsearch │
│   Topics    │    │  Microservice       │    └───────────────┘
└─────────────┘    │  - Sentiment        │    ┌───────────────┐
                   │  - NER              │───▶│    Neo4j      │
                   │  - Topic            │    └───────────────┘
                   └─────────────────────┘
```

---

# خدمة التحليلات الذكية المصغرة

_التوثيق باللغة العربية_

## نظرة عامة

خدمة التحليلات الذكية المصغرة هي خدمة تعتمد على FastAPI لتحليل البيانات النصية باستخدام نماذج معالجة اللغة الطبيعية والذكاء الاصطناعي لتوليد رؤى قابلة للتنفيذ. تستهلك الخدمة البيانات الاجتماعية الخام والبيانات المستخرجة من Kafka، وتعالجها باستخدام نماذج تعلم آلي لتحليل المشاعر، والتعرف على الكيانات المسماة، وتصنيف الموضوعات، وتخرج النتائج إلى Elasticsearch وNeo4j.

## الميزات

- **دعم متعدد اللغات**: معالجة النصوص العربية والإنجليزية باستخدام نماذج AraBERT/mBERT
- **تحليل المشاعر**: تحديد مشاعر النص (إيجابي، سلبي، محايد)
- **التعرف على الكيانات المسماة**: استخراج كيانات مثل الشخص والموقع والمنظمة
- **تصنيف الموضوعات**: تصنيف النص إلى موضوعات مثل الجرائم الإلكترونية والإرهاب والجرائم المالية وغيرها
- **تكامل Kafka**: استهلاك الرسائل من مواضيع `raw_social_data` و `raw_scraped_data`
- **إخراج البيانات**: كتابة البيانات المعززة إلى Elasticsearch وإنشاء رسوم بيانية للكيانات في Neo4j

## التثبيت

### المتطلبات الأساسية

- Python 3.8+
- Kafka
- Elasticsearch
- Neo4j

### الإعداد

1. استنساخ المستودع
2. تثبيت التبعيات:

```bash
pip install -r requirements.txt
```

3. تعيين متغيرات البيئة (أو إنشاء ملف `.env`):

```
# Kafka
KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# Elasticsearch
ELASTICSEARCH_HOSTS=localhost:9200
ELASTICSEARCH_USERNAME=elastic
ELASTICSEARCH_PASSWORD=changeme

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=test

# NLP Models
SENTIMENT_MODEL=asafaya/bert-base-arabic-sentiment
NER_MODEL=aubmindlab/bert-base-arabertv02-ner
TOPIC_MODEL=facebook/bart-large-mnli
```

## الاستخدام

### تشغيل الخدمة

```bash
uvicorn main:app --reload
```

ستكون الخدمة متاحة على http://localhost:8000

### نقاط النهاية API

- `GET /health` - نقطة نهاية فحص الصحة
- `POST /test` - نقطة نهاية اختبار لتحليل إدخال نصي واحد
- `GET /models` - قائمة بنماذج معالجة اللغة الطبيعية المتاحة
- `POST /start-processing` - بدء معالجة الرسائل من Kafka
- `POST /stop-processing` - إيقاف معالجة الرسائل من Kafka
- `GET /processing-status` - الحصول على الحالة الحالية لمعالجة Kafka

### مثال طلب

```bash
curl -X POST "http://localhost:8000/test" \
     -H "Content-Type: application/json" \
     -d '{"text":"سرق المجرم الإلكتروني بيانات من مقر الإنتربول في ليون، فرنسا.", "source":"news"}'
```

### مثال استجابة

```json
{
  "source": "news",
  "text": "سرق المجرم الإلكتروني بيانات من مقر الإنتربول في ليون، فرنسا.",
  "sentiment": { 
    "label": "negative", 
    "confidence": 0.91 
  },
  "entities": [
    {"type": "PERSON", "value": "المجرم الإلكتروني"},
    {"type": "ORGANIZATION", "value": "الإنتربول"},
    {"type": "LOCATION", "value": "ليون"},
    {"type": "LOCATION", "value": "فرنسا"}
  ],
  "topic": "cybercrime",
  "timestamp": "2025-05-07T10:00:00Z"
}
```

## دوكر

بناء وتشغيل حاوية Docker:

```bash
docker build -t ai_analytics_service .
docker run -p 8000:8000 ai_analytics_service
```

## الهيكل المعماري

```
┌─────────────┐    ┌─────────────────────┐    ┌───────────────┐
│   Kafka     │───▶│  AI Analytics       │───▶│ Elasticsearch │
│   Topics    │    │  Microservice       │    └───────────────┘
└─────────────┘    │  - Sentiment        │    ┌───────────────┐
                   │  - NER              │───▶│    Neo4j      │
                   │  - Topic            │    └───────────────┘
                   └─────────────────────┘
```


# SOCMINT Platform Deployment & Testing Guide

## Overview

This guide provides step-by-step instructions for deploying and validating the SOCMINT (Social Media Intelligence) SaaS platform using Docker Compose on an Ubuntu Server. The deployment process is automated through the `deploy_and_test.sh` script, which performs comprehensive validation across all system components.

## System Requirements

- **Operating System**: Ubuntu Server 20.04 or newer
- **Hardware**:
  - CPU: 16 cores (minimum recommended)
  - RAM: 32 GB (minimum recommended)
  - Storage: 512 GB SSD
- **Software**:
  - Docker Engine
  - Docker Compose
- **Network**: Internet access for pulling containers and UAE PASS sandbox testing

## Pre-Deployment Checklist

1. Ensure Docker and Docker Compose are installed:
   ```bash
   docker --version
   docker-compose --version
   ```

2. Verify system resources meet the minimum requirements:
   ```bash
   # Check CPU cores
   nproc
   
   # Check RAM
   free -h
   
   # Check disk space
   df -h
   ```

3. Ensure all required environment variables are set in the `.env` file:
   - `ELASTIC_PASSWORD`
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`
   - `NEO4J_AUTH`

## Deployment Process

### 1. Clone the Repository

If you haven't already, clone the SOCMINT repository to your server:

```bash
# Example (replace with actual repository URL)
git clone https://github.com/your-organization/socmint-platform.git
cd socmint-platform
```

### 2. Run the Deployment Script

Make the deployment script executable and run it:

```bash
chmod +x deploy_and_test.sh
./deploy_and_test.sh
```

The script will automatically:

1. Check system requirements
2. Start all services using Docker Compose
3. Validate infrastructure components
4. Test Kafka and database connectivity
5. Verify backend API endpoints
6. Check frontend accessibility
7. Validate TOR integration
8. Perform final review and create database backups

## Validation Phases

The deployment script performs validation in six phases:

### Phase 1: Infrastructure Validation

- Starts all Docker containers
- Verifies container status
- Checks network connectivity
- Tests access to all services (Frontend, Backend API, Elasticsearch, PostgreSQL, Neo4j)

### Phase 2: Kafka & Database Testing

- Lists Kafka topics
- Tests message production and consumption
- Verifies PostgreSQL tables exist and are accessible

### Phase 3: Backend API Testing

- Tests all critical API endpoints:
  - `/collect/twitter`
  - `/scrape/darkweb`
  - `/run-analysis`
  - `/generate-report`
  - `/verify/<report_id>`
  - `/auth/uaepass/login`

### Phase 4: Frontend Testing

- Verifies frontend accessibility
- Provides instructions for manual testing of:
  - Role-based views (Admin, Analyst, Viewer)
  - Language switching (Arabic, Farsi, Russian)
  - UAE PASS integration

### Phase 5: TOR Validation

- Tests TOR connectivity
- Verifies dark web scraping functionality

### Phase 6: Final Review

- Checks service logs for errors
- Monitors resource usage
- Creates database backups
- Verifies security configurations

## Post-Deployment Steps

1. **Security Hardening**:
   - Configure HTTPS for all public-facing services
   - Review and restrict network access
   - Implement proper authentication for all services

2. **Monitoring Setup**:
   - Configure monitoring tools (e.g., Prometheus, Grafana)
   - Set up alerting for critical services

3. **Regular Backups**:
   - Implement automated backup schedule for all databases
   - Test backup restoration process

## Troubleshooting

### Common Issues

1. **Container Startup Failures**:
   - Check container logs: `docker-compose logs <service_name>`
   - Verify environment variables in `.env` file

2. **Network Connectivity Issues**:
   - Ensure `socmint_network` is created: `docker network ls`
   - Check container network settings: `docker network inspect socmint_network`

3. **API Endpoint Failures**:
   - Check backend logs: `docker-compose logs backend`
   - Verify database connectivity

4. **TOR Connection Issues**:
   - Check TOR container logs: `docker-compose logs tor`
   - Verify TOR service is running: `docker-compose ps tor`

## Support

For additional support or to report issues, please contact the SOCMINT platform team.

---

# دليل نشر واختبار منصة SOCMINT

## نظرة عامة

يوفر هذا الدليل تعليمات خطوة بخطوة لنشر والتحقق من منصة SOCMINT (استخبارات وسائل التواصل الاجتماعي) كخدمة SaaS باستخدام Docker Compose على خادم Ubuntu. تتم أتمتة عملية النشر من خلال البرنامج النصي `deploy_and_test.sh`، الذي يقوم بإجراء تحقق شامل عبر جميع مكونات النظام.

## متطلبات النظام

- **نظام التشغيل**: Ubuntu Server 20.04 أو أحدث
- **الأجهزة**:
  - وحدة المعالجة المركزية: 16 نواة (الحد الأدنى الموصى به)
  - ذاكرة الوصول العشوائي: 32 جيجابايت (الحد الأدنى الموصى به)
  - التخزين: 512 جيجابايت SSD
- **البرمجيات**:
  - Docker Engine
  - Docker Compose
- **الشبكة**: اتصال بالإنترنت لسحب الحاويات واختبار UAE PASS

## قائمة التحقق قبل النشر

1. تأكد من تثبيت Docker و Docker Compose:
   ```bash
   docker --version
   docker-compose --version
   ```

2. تحقق من أن موارد النظام تلبي الحد الأدنى من المتطلبات:
   ```bash
   # التحقق من نوى وحدة المعالجة المركزية
   nproc
   
   # التحقق من ذاكرة الوصول العشوائي
   free -h
   
   # التحقق من مساحة القرص
   df -h
   ```

3. تأكد من تعيين جميع متغيرات البيئة المطلوبة في ملف `.env`:
   - `ELASTIC_PASSWORD`
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`
   - `NEO4J_AUTH`

## عملية النشر

### 1. استنساخ المستودع

إذا لم تقم بذلك بالفعل، قم باستنساخ مستودع SOCMINT إلى الخادم الخاص بك:

```bash
# مثال (استبدل برابط المستودع الفعلي)
git clone https://github.com/your-organization/socmint-platform.git
cd socmint-platform
```

### 2. تشغيل برنامج النشر

اجعل برنامج النشر قابلاً للتنفيذ وقم بتشغيله:

```bash
chmod +x deploy_and_test.sh
./deploy_and_test.sh
```

سيقوم البرنامج النصي تلقائيًا بما يلي:

1. التحقق من متطلبات النظام
2. بدء جميع الخدمات باستخدام Docker Compose
3. التحقق من مكونات البنية التحتية
4. اختبار اتصال Kafka وقاعدة البيانات
5. التحقق من نقاط نهاية واجهة برمجة التطبيقات الخلفية
6. التحقق من إمكانية الوصول إلى الواجهة الأمامية
7. التحقق من تكامل TOR
8. إجراء المراجعة النهائية وإنشاء نسخ احتياطية لقاعدة البيانات

## مراحل التحقق

يقوم برنامج النشر بإجراء التحقق في ست مراحل:

### المرحلة 1: التحقق من البنية التحتية

- بدء تشغيل جميع حاويات Docker
- التحقق من حالة الحاوية
- التحقق من اتصال الشبكة
- اختبار الوصول إلى جميع الخدمات (الواجهة الأمامية، واجهة برمجة التطبيقات الخلفية، Elasticsearch، PostgreSQL، Neo4j)

### المرحلة 2: اختبار Kafka وقاعدة البيانات

- سرد مواضيع Kafka
- اختبار إنتاج واستهلاك الرسائل
- التحقق من وجود جداول PostgreSQL وإمكانية الوصول إليها

### المرحلة 3: اختبار واجهة برمجة التطبيقات الخلفية

- اختبار جميع نقاط نهاية واجهة برمجة التطبيقات الحرجة:
  - `/collect/twitter`
  - `/scrape/darkweb`
  - `/run-analysis`
  - `/generate-report`
  - `/verify/<report_id>`
  - `/auth/uaepass/login`

### المرحلة 4: اختبار الواجهة الأمامية

- التحقق من إمكانية الوصول إلى الواجهة الأمامية
- تقديم تعليمات للاختبار اليدوي لـ:
  - العروض المستندة إلى الأدوار (المسؤول، المحلل، المشاهد)
  - تبديل اللغة (العربية، الفارسية، الروسية)
  - تكامل UAE PASS

### المرحلة 5: التحقق من TOR

- اختبار اتصال TOR
- التحقق من وظيفة كشط الويب المظلم

### المرحلة 6: المراجعة النهائية

- التحقق من سجلات الخدمة بحثًا عن الأخطاء
- مراقبة استخدام الموارد
- إنشاء نسخ احتياطية لقاعدة البيانات
- التحقق من تكوينات الأمان

## خطوات ما بعد النشر

1. **تقوية الأمان**:
   - تكوين HTTPS لجميع الخدمات المواجهة للجمهور
   - مراجعة وتقييد الوصول إلى الشبكة
   - تنفيذ المصادقة المناسبة لجميع الخدمات

2. **إعداد المراقبة**:
   - تكوين أدوات المراقبة (مثل Prometheus، Grafana)
   - إعداد التنبيهات للخدمات الحرجة

3. **النسخ الاحتياطية المنتظمة**:
   - تنفيذ جدول النسخ الاحتياطي الآلي لجميع قواعد البيانات
   - اختبار عملية استعادة النسخ الاحتياطي

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

1. **فشل بدء تشغيل الحاوية**:
   - تحقق من سجلات الحاوية: `docker-compose logs <service_name>`
   - تحقق من متغيرات البيئة في ملف `.env`

2. **مشكلات اتصال الشبكة**:
   - تأكد من إنشاء `socmint_network`: `docker network ls`
   - تحقق من إعدادات شبكة الحاوية: `docker network inspect socmint_network`

3. **فشل نقطة نهاية واجهة برمجة التطبيقات**:
   - تحقق من سجلات الخلفية: `docker-compose logs backend`
   - تحقق من اتصال قاعدة البيانات

4. **مشكلات اتصال TOR**:
   - تحقق من سجلات حاوية TOR: `docker-compose logs tor`
   - تحقق من تشغيل خدمة TOR: `docker-compose ps tor`

## الدعم

للحصول على دعم إضافي أو للإبلاغ عن المشكلات، يرجى الاتصال بفريق منصة SOCMINT.



# Social Media Manager Microservice

## Overview
This microservice integrates the open-source Postiz App as a multi-tenant social media management solution within the SOCMINT platform. It enables each tenant to securely manage their social media accounts (Facebook, Twitter, LinkedIn) for scheduling, publishing, and analytics — isolated per customer.

## Features
- **Multi-Tenant Authentication**: JWT validation with tenant isolation
- **Social Media Integration**: OAuth2 for multiple platforms
- **Post Scheduling**: Create and schedule posts with status monitoring
- **Analytics**: Track engagement metrics and generate reports
- **Secure Token Management**: Encrypted storage with periodic refresh

## Architecture

### Directory Structure
```
social_media_manager/
├── Dockerfile
├── requirements.txt
├── main.py
├── routes/
│   ├── auth.py
│   ├── posts.py
│   ├── scheduler.py
│   └── analytics.py
├── models/
│   ├── database.py
│   ├── user.py
│   ├── tenant.py
│   ├── post.py
│   └── campaign.py
└── utils/
    ├── token_verification.py
    └── oauth_handler.py
```

### API Endpoints
- `POST /api/v1/connect/account` - Connect social media account
- `POST /api/v1/schedule` - Schedule a post
- `GET /api/v1/posts` - Get all posts for a tenant
- `GET /api/v1/analytics/campaign/{id}` - Get campaign analytics

### Database Schema
- `social_accounts` - Store social media account credentials
- `posts` - Store post content and scheduling information
- `campaigns` - Store campaign data and metrics

## Setup and Deployment

### Prerequisites
- Python 3.10+
- PostgreSQL database
- Redis (for Celery)

### Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables (see `.env.example`)
4. Run migrations: `alembic upgrade head`
5. Start the server: `uvicorn main:app --reload`

### Docker Deployment
```bash
docker-compose up -d
```

## Security Considerations
- All API endpoints require valid JWT authentication
- Tenant isolation enforced via `tenant_id`
- Social media tokens encrypted at rest
- HTTPS required for all communications

---

# خدمة إدارة وسائل التواصل الاجتماعي المصغرة

## نظرة عامة
تدمج هذه الخدمة المصغرة تطبيق Postiz مفتوح المصدر كحل متعدد المستأجرين لإدارة وسائل التواصل الاجتماعي ضمن منصة SOCMINT. تمكن كل مستأجر من إدارة حسابات وسائل التواصل الاجتماعي الخاصة به (فيسبوك، تويتر، لينكد إن) بشكل آمن للجدولة والنشر والتحليلات — معزولة لكل عميل.

## الميزات
- **مصادقة متعددة المستأجرين**: التحقق من JWT مع عزل المستأجر
- **تكامل وسائل التواصل الاجتماعي**: OAuth2 لمنصات متعددة
- **جدولة المنشورات**: إنشاء وجدولة المنشورات مع مراقبة الحالة
- **التحليلات**: تتبع مقاييس المشاركة وإنشاء التقارير
- **إدارة الرموز الآمنة**: تخزين مشفر مع تحديث دوري

## الهيكل

### هيكل الدليل
```
social_media_manager/
├── Dockerfile
├── requirements.txt
├── main.py
├── routes/
│   ├── auth.py
│   ├── posts.py
│   ├── scheduler.py
│   └── analytics.py
├── models/
│   ├── database.py
│   ├── user.py
│   ├── tenant.py
│   ├── post.py
│   └── campaign.py
└── utils/
    ├── token_verification.py
    └── oauth_handler.py
```

### نقاط النهاية API
- `POST /api/v1/connect/account` - ربط حساب وسائل التواصل الاجتماعي
- `POST /api/v1/schedule` - جدولة منشور
- `GET /api/v1/posts` - الحصول على جميع المنشورات لمستأجر
- `GET /api/v1/analytics/campaign/{id}` - الحصول على تحليلات الحملة

### مخطط قاعدة البيانات
- `social_accounts` - تخزين بيانات اعتماد حساب وسائل التواصل الاجتماعي
- `posts` - تخزين محتوى المنشور ومعلومات الجدولة
- `campaigns` - تخزين بيانات الحملة والمقاييس

## الإعداد والنشر

### المتطلبات المسبقة
- Python 3.10+
- قاعدة بيانات PostgreSQL
- Redis (لـ Celery)

### التثبيت
1. استنساخ المستودع
2. تثبيت التبعيات: `pip install -r requirements.txt`
3. تعيين متغيرات البيئة (انظر `.env.example`)
4. تشغيل الترحيلات: `alembic upgrade head`
5. بدء الخادم: `uvicorn main:app --reload`

### نشر Docker
```bash
docker-compose up -d
```

## اعتبارات الأمان
- تتطلب جميع نقاط نهاية API مصادقة JWT صالحة
- فرض عزل المستأجر عبر `tenant_id`
- تشفير رموز وسائل التواصل الاجتماعي في وضع الراحة
- HTTPS مطلوب لجميع الاتصالات


# SOCMINT Visual Identity System

_RHAL – عجمان للتقنيات المتقدمة_

## Overview

This document defines the complete visual identity system for the SOCMINT platform. It establishes a consistent, professional identity across all user interfaces, dashboards, reports, and communications that reflects the sovereignty, intelligence, and UAE heritage of the product.

---

## 1. Color Palette

### Primary Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| RHAL Green | `#00A651` | rgb(0, 166, 81) | Primary brand color, buttons, active states |
| RHAL Dark | `#1A1A1A` | rgb(26, 26, 26) | Backgrounds, text |

### Secondary Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| White | `#FFFFFF` | rgb(255, 255, 255) | Text, backgrounds |
| Light Gray | `#F5F5F5` | rgb(245, 245, 245) | Backgrounds, dividers |
| Medium Gray | `#CCCCCC` | rgb(204, 204, 204) | Disabled states, borders |
| Dark Gray | `#666666` | rgb(102, 102, 102) | Secondary text |

### Accent Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| UAE Red | `#EF3340` | rgb(239, 51, 64) | Alerts, errors, critical notifications |
| Success | `#4CAF50` | rgb(76, 175, 80) | Success states, confirmations |
| Warning | `#FFC107` | rgb(255, 193, 7) | Warnings, cautions |
| Info | `#2196F3` | rgb(33, 150, 243) | Information, help |

### Color Tokens (Flutter)

```dart
class SOCMINTColors {
  // Primary
  static const Color rhalGreen = Color(0xFF00A651);
  static const Color rhalDark = Color(0xFF1A1A1A);
  
  // Secondary
  static const Color white = Color(0xFFFFFFFF);
  static const Color lightGray = Color(0xFFF5F5F5);
  static const Color mediumGray = Color(0xFFCCCCCC);
  static const Color darkGray = Color(0xFF666666);
  
  // Accent
  static const Color uaeRed = Color(0xFFEF3340);
  static const Color success = Color(0xFF4CAF50);
  static const Color warning = Color(0xFFFFC107);
  static const Color info = Color(0xFF2196F3);
}
```

### Color Tokens (Tailwind CSS)

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'rhal-green': '#00A651',
        'rhal-dark': '#1A1A1A',
        'light-gray': '#F5F5F5',
        'medium-gray': '#CCCCCC',
        'dark-gray': '#666666',
        'uae-red': '#EF3340',
      }
    }
  }
}
```

---

## 2. Typography

### Font Families

| Language | Primary Font | Fallback |
|----------|--------------|----------|
| Arabic | Dubai Font | Noto Kufi Arabic |
| English/Latin | Montserrat | Source Sans Pro |

### Font Weights

| Weight Name | Weight Value | Usage |
|-------------|--------------|-------|
| Light | 300 | Body text (long form) |
| Regular | 400 | Body text, UI elements |
| Medium | 500 | Emphasis, subheadings |
| SemiBold | 600 | Buttons, important UI elements |
| Bold | 700 | Headings, titles |

### Typography Scale

| Element | Size (px) | Weight | Line Height | Usage |
|---------|-----------|--------|-------------|-------|
| H1 | 32px | Bold | 1.2 | Main page titles |
| H2 | 24px | Bold | 1.3 | Section headings |
| H3 | 20px | SemiBold | 1.4 | Subsection headings |
| H4 | 18px | SemiBold | 1.4 | Card titles |
| Body 1 | 16px | Regular | 1.5 | Primary body text |
| Body 2 | 14px | Regular | 1.5 | Secondary body text |
| Caption | 12px | Regular | 1.4 | Labels, captions |
| Button | 16px | SemiBold | 1.2 | Button text |

### Typography Implementation (Flutter)

```dart
class SOCMINTTextStyles {
  // Arabic
  static const TextStyle arabicH1 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 32,
    fontWeight: FontWeight.w700,
    height: 1.2,
  );
  
  // English
  static const TextStyle englishH1 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 32,
    fontWeight: FontWeight.w700,
    height: 1.2,
  );
  
  // Add all other text styles following the same pattern
}
```

---

## 3. UI Elements

### Buttons

#### Primary Button
- Background: RHAL Green (#00A651)
- Text: White
- Border Radius: 8px
- Padding: 12px 24px
- Text Style: 16px SemiBold
- Hover Effect: Slight darkening of green + subtle glow
- Disabled State: Medium Gray background

#### Secondary Button
- Background: Transparent
- Text: RHAL Green
- Border: 1px RHAL Green
- Border Radius: 8px
- Padding: 12px 24px
- Text Style: 16px SemiBold
- Hover Effect: Light green background
- Disabled State: Medium Gray text and border

#### Tertiary Button (Text Button)
- Background: Transparent
- Text: RHAL Green
- Border: None
- Padding: 12px 16px
- Text Style: 16px SemiBold
- Hover Effect: Light green text underline
- Disabled State: Medium Gray text

### Cards

- Background: White
- Border Radius: 12px
- Shadow: 0px 2px 8px rgba(0, 0, 0, 0.1)
- Padding: 16px
- Title: H4 style
- Content: Body 1 or Body 2 style

### Form Elements

#### Text Input
- Background: White
- Border: 1px Medium Gray
- Border Radius: 8px
- Padding: 12px 16px
- Text: Body 1
- Focus State: RHAL Green border
- Error State: UAE Red border

#### Dropdown
- Same styling as Text Input
- Dropdown Icon: Dark Gray
- Options Menu: White background, 4px border radius

#### Checkbox
- Size: 20px × 20px
- Border: 1px Medium Gray
- Border Radius: 4px
- Checked State: RHAL Green background, white checkmark

### Navigation

#### Sidebar
- Background: RHAL Dark (#1A1A1A)
- Text: White
- Active Item: RHAL Green left border, light green background
- Hover State: Slight gray background
- Icon: 24px, aligned with text

#### Top Bar
- Background: White
- Border Bottom: 1px Light Gray
- Height: 64px
- Logo: Left aligned
- User Menu: Right aligned

---

## 4. Logo Usage

### Primary Logo
- The RHAL logo consists of the Arabic text "رحّال" with a green bar above it
- Primary version is white text on black background
- The green bar must always be preserved in the RHAL Green color (#00A651)

### Clear Space
- Maintain clear space around the logo equal to the height of the letter "ر" in the logo
- No elements should intrude into this clear space

### Size Restrictions
- Minimum size: 24px height for digital use
- Minimum size: 10mm height for print use

### Incorrect Usage
- Do not distort or stretch the logo
- Do not change the colors of the logo elements
- Do not rotate or flip the logo
- Do not remove the green bar
- Do not add effects (shadows, glows, etc.) to the logo

### Logo Variants
1. Primary: White on black
2. Reversed: Black on white
3. Monochrome: All white (for dark backgrounds)
4. Monochrome: All black (for light backgrounds)

---

## 5. Layout Guidelines

### Dashboard Layout

#### Structure
- Left Sidebar: 240px width, RHAL Dark background
- Top Bar: 64px height, white background
- Main Content Area: Remaining space, Light Gray background

#### Grid System
- 12-column grid
- 24px gutters
- Responsive breakpoints:
  - Mobile: < 768px
  - Tablet: 768px - 1024px
  - Desktop: > 1024px

#### Card Layout
- Cards should align to the grid
- Standard card sizes:
  - 1/4 width (3 columns)
  - 1/3 width (4 columns)
  - 1/2 width (6 columns)
  - Full width (12 columns)

#### Spacing System
- Base unit: 8px
- Spacing scale: 8px, 16px, 24px, 32px, 48px, 64px
- Consistent spacing between sections: 32px
- Consistent spacing between cards: 24px
- Internal card padding: 16px

---

## 6. Landing Page Design

### Structure

1. **Hero Section**
   - Centered logo
   - Tagline: "منصة الاستخبارات السيادية متعددة القنوات"
   - Language switch (ar/en) at top right
   - CTA button: "Request Demo" or "Login"

2. **About Section**
   - Brief description of SOCMINT
   - Key features with icons
   - UAE-focused imagery

3. **Features Section**
   - Grid of feature cards
   - Each card with icon, title, and brief description

4. **Dashboard Preview**
   - Screenshot or mockup of the dashboard
   - Annotations highlighting key features

5. **Subscribe Section**
   - Email subscription form
   - Contact information

6. **Footer**
   - Logo
   - Navigation links
   - Social media links
   - Copyright information

---

## 7. Document Style Guide

### Report Template

#### Cover Page
- RHAL logo (top center)
- Report title (H1, centered)
- Date and classification (Body 2, centered)
- Generated by SOCMINT (caption, bottom center)

#### Interior Pages
- Header: RHAL logo (small, top left), page number (top right)
- Section headings: H2
- Subsection headings: H3
- Body text: Body 1
- Tables: Clean borders, header row in RHAL Green
- Charts: SOCMINT color palette, consistent styling
- Footer: Classification, date, page number

### Presentation Template

#### Title Slide
- RHAL logo (center)
- Presentation title (H1)
- Subtitle or date (H3)
- Presenter information (Body 1)

#### Content Slides
- Header: RHAL logo (small, top left), slide title (top)
- Content area: Clean, minimal
- Text hierarchy: H2 for titles, Body 1 for content
- Footer: Classification, date, slide number

---

## 8. Icons and Favicon

### Icon Style
- Line weight: 2px
- Corner radius: 2px
- Style: Outlined with occasional solid elements
- Size: 24px × 24px (standard), 16px × 16px (small)

### Favicon
- Square version of the RHAL logo
- Sizes: 512×512, 192×192, 48×48, 32×32, 16×16
- Format: SVG (primary), PNG (fallback)

### App Icon
- Square with rounded corners (12px radius)
- RHAL logo centered
- RHAL Green background
- Sizes: 512×512, 192×192, 48×48

---

## 9. Implementation Guidelines

### Flutter Implementation

```dart
// Example theme implementation
ThemeData socmintLightTheme() {
  return ThemeData(
    primaryColor: SOCMINTColors.rhalGreen,
    scaffoldBackgroundColor: SOCMINTColors.lightGray,
    appBarTheme: AppBarTheme(
      backgroundColor: SOCMINTColors.white,
      foregroundColor: SOCMINTColors.rhalDark,
      elevation: 1,
    ),
    textTheme: TextTheme(
      // Map all text styles here
    ),
    // Other theme properties
  );
}

ThemeData socmintDarkTheme() {
  return ThemeData(
    primaryColor: SOCMINTColors.rhalGreen,
    scaffoldBackgroundColor: SOCMINTColors.rhalDark,
    // Dark theme properties
  );
}
```

### Web Implementation (Tailwind)

```html
<!-- Example button implementation -->
<button class="bg-rhal-green text-white font-semibold py-3 px-6 rounded-lg hover:bg-rhal-green-dark transition duration-300">
  Login with UAE PASS
</button>
```

---

## 10. RTL Considerations

- All layouts must support RTL (Right-to-Left) for Arabic
- Text alignment should automatically adjust based on language
- Icons that indicate direction (arrows, etc.) should flip in RTL mode
- Form elements should have labels positioned correctly in RTL

---

## 11. Accessibility Guidelines

- Color contrast must meet WCAG AA standards (minimum 4.5:1 for normal text)
- Interactive elements must have sufficient touch targets (minimum 44×44px)
- All UI elements must be accessible via keyboard
- Text should be resizable without breaking layouts
- Screen reader support for all UI elements

---

# نظام الهوية البصرية لمنصة SOCMINT

_رحّال – عجمان للتقنيات المتقدمة_

## نظرة عامة

تحدد هذه الوثيقة نظام الهوية البصرية الكامل لمنصة SOCMINT. وهي تؤسس هوية متسقة واحترافية عبر جميع واجهات المستخدم ولوحات المعلومات والتقارير والاتصالات التي تعكس السيادة والذكاء والتراث الإماراتي للمنتج.

---

## ١. لوحة الألوان

### الألوان الأساسية

| اسم اللون | رمز Hex | RGB | الاستخدام |
|------------|----------|-----|-------|
| أخضر رحّال | `#00A651` | rgb(0, 166, 81) | لون العلامة التجارية الأساسي، الأزرار، الحالات النشطة |
| داكن رحّال | `#1A1A1A` | rgb(26, 26, 26) | الخلفيات، النصوص |

### الألوان الثانوية

| اسم اللون | رمز Hex | RGB | الاستخدام |
|------------|----------|-----|-------|
| أبيض | `#FFFFFF` | rgb(255, 255, 255) | النصوص، الخلفيات |
| رمادي فاتح | `#F5F5F5` | rgb(245, 245, 245) | الخلفيات، الفواصل |
| رمادي متوسط | `#CCCCCC` | rgb(204, 204, 204) | الحالات المعطلة، الحدود |
| رمادي داكن | `#666666` | rgb(102, 102, 102) | النصوص الثانوية |

### ألوان التأكيد

| اسم اللون | رمز Hex | RGB | الاستخدام |
|------------|----------|-----|-------|
| أحمر إماراتي | `#EF3340` | rgb(239, 51, 64) | التنبيهات، الأخطاء، الإشعارات الحرجة |
| نجاح | `#4CAF50` | rgb(76, 175, 80) | حالات النجاح، التأكيدات |
| تحذير | `#FFC107` | rgb(255, 193, 7) | التحذيرات، التنبيهات |
| معلومات | `#2196F3` | rgb(33, 150, 243) | المعلومات، المساعدة |

---

## ٢. الطباعة

### عائلات الخطوط

| اللغة | الخط الأساسي | الخط البديل |
|----------|--------------|----------|
| العربية | خط دبي | نوتو كوفي العربي |
| الإنجليزية/اللاتينية | مونتسيرات | سورس سانس برو |

### أوزان الخطوط

| اسم الوزن | قيمة الوزن | الاستخدام |
|-------------|--------------|-------|
| خفيف | 300 | نص الجسم (النموذج الطويل) |
| عادي | 400 | نص الجسم، عناصر واجهة المستخدم |
| متوسط | 500 | التأكيد، العناوين الفرعية |
| شبه غامق | 600 | الأزرار، عناصر واجهة المستخدم المهمة |
| غامق | 700 | العناوين، العناوين الرئيسية |

---

## ٣. عناصر واجهة المستخدم

### الأزرار

#### الزر الأساسي
- الخلفية: أخضر رحّال (#00A651)
- النص: أبيض
- نصف قطر الحدود: 8 بكسل
- الحشو: 12 بكسل 24 بكسل
- نمط النص: 16 بكسل شبه غامق
- تأثير التحويم: تعتيم طفيف للأخضر + توهج خفيف
- حالة التعطيل: خلفية رمادية متوسطة

#### الزر الثانوي
- الخلفية: شفافة
- النص: أخضر رحّال
- الحدود: 1 بكسل أخضر رحّال
- نصف قطر الحدود: 8 بكسل
- الحشو: 12 بكسل 24 بكسل
- نمط النص: 16 بكسل شبه غامق
- تأثير التحويم: خلفية خضراء فاتحة
- حالة التعطيل: نص وحدود رمادية متوسطة

---

## ٤. استخدام الشعار

### الشعار الأساسي
- يتكون شعار رحّال من النص العربي "رحّال" مع شريط أخضر فوقه
- النسخة الأساسية هي نص أبيض على خلفية سوداء
- يجب الحفاظ دائمًا على الشريط الأخضر بلون أخضر رحّال (#00A651)

### المساحة الخالية
- الحفاظ على مساحة خالية حول الشعار تساوي ارتفاع حرف "ر" في الشعار
- لا ينبغي أن تتعدى أي عناصر على هذه المساحة الخالية

---

## ٥. إرشادات التخطيط

### تخطيط لوحة المعلومات

#### الهيكل
- الشريط الجانبي الأيسر: عرض 240 بكسل، خلفية داكنة رحّال
- الشريط العلوي: ارتفاع 64 بكسل، خلفية بيضاء
- منطقة المحتوى الرئيسية: المساحة المتبقية، خلفية رمادية فاتحة

---

هذه الوثيقة تحدد المعايير الأساسية للهوية البصرية لمنصة SOCMINT، وتوفر إرشادات واضحة للمطورين والمصممين لضمان تجربة مستخدم متسقة وجذابة تعكس هوية العلامة التجارية.

# SOCMINT Visual Identity System

_RHAL – عجمان للتقنيات المتقدمة_

## Overview

This directory contains the complete visual identity system for the SOCMINT platform. It establishes a consistent, professional identity across all user interfaces, dashboards, reports, and communications that reflects the sovereignty, intelligence, and UAE heritage of the product.

## Directory Contents

- **socmint_design_system.md**: Comprehensive documentation of the entire design system
- **socmint_logo_guidelines.md**: Detailed guidelines for logo usage
- **socmint_theme.dart**: Flutter implementation of colors and typography
- **socmint_ui_components.dart**: Reusable UI components based on the design system
- **socmint_web_tokens.js**: CSS variables and Tailwind configuration for web implementation
- **index.dart**: Exports all Flutter components for easy import

## Quick Start

### Flutter Implementation

1. Import the design system in your Flutter files:

```dart
import 'package:socmint/design_system/index.dart';
```

2. Apply the theme in your MaterialApp:

```dart
MaterialApp(
  theme: SOCMINTTheme.lightTheme(),
  darkTheme: SOCMINTTheme.darkTheme(),
  // ...
)
```

3. Use the components in your UI:

```dart
SOCMINTPrimaryButton(
  text: 'Login with UAE PASS',
  onPressed: () => login(),
  icon: Icons.login,
)
```

### Web Implementation

1. Include the CSS variables in your HTML:

```html
<style>
  /* Copy the CSS variables from socmint_web_tokens.js */
</style>
```

2. Configure Tailwind (if using):

```js
// tailwind.config.js
const socmintTokens = require('./socmint_web_tokens.js');

module.exports = {
  theme: socmintTokens.tailwindConfig.theme,
  variants: socmintTokens.tailwindConfig.variants,
  plugins: socmintTokens.tailwindConfig.plugins,
};
```

3. Use the utility classes in your HTML:

```html
<button class="bg-rhal-green text-white font-semibold py-3 px-6 rounded-md hover:bg-opacity-90 transition duration-300">
  Login with UAE PASS
</button>
```

## Design Principles

1. **UAE Heritage**: Reflects Emirati culture and values
2. **Professionalism**: Clean, minimal design for intelligence applications
3. **Consistency**: Unified experience across all touchpoints
4. **Accessibility**: Supports RTL languages and meets WCAG standards
5. **Adaptability**: Works across devices and platforms

## Color Palette

- **Primary**: RHAL Green (#00A651)
- **Secondary**: White, Black, Gray shades
- **Accent**: UAE Red (#EF3340) for alerts and errors

## Typography

- **Arabic**: Dubai Font / Noto Kufi Arabic
- **English**: Montserrat / Source Sans Pro

## Contact

For questions about the design system, contact the SOCMINT design team.

---

# نظام الهوية البصرية لمنصة SOCMINT

_رحّال – عجمان للتقنيات المتقدمة_

## نظرة عامة

يحتوي هذا الدليل على نظام الهوية البصرية الكامل لمنصة SOCMINT. يؤسس هوية متسقة واحترافية عبر جميع واجهات المستخدم ولوحات المعلومات والتقارير والاتصالات التي تعكس السيادة والذكاء والتراث الإماراتي للمنتج.

## محتويات الدليل

- **socmint_design_system.md**: توثيق شامل لنظام التصميم بأكمله
- **socmint_logo_guidelines.md**: إرشادات مفصلة لاستخدام الشعار
- **socmint_theme.dart**: تنفيذ Flutter للألوان والطباعة
- **socmint_ui_components.dart**: مكونات واجهة المستخدم القابلة لإعادة الاستخدام بناءً على نظام التصميم
- **socmint_web_tokens.js**: متغيرات CSS وتكوين Tailwind للتنفيذ على الويب
- **index.dart**: يصدر جميع مكونات Flutter لسهولة الاستيراد

## مبادئ التصميم

1. **التراث الإماراتي**: يعكس الثقافة والقيم الإماراتية
2. **الاحترافية**: تصميم نظيف وبسيط لتطبيقات الاستخبارات
3. **الاتساق**: تجربة موحدة عبر جميع نقاط التواصل
4. **إمكانية الوصول**: يدعم لغات RTL ويلبي معايير WCAG
5. **القابلية للتكيف**: يعمل عبر الأجهزة والمنصات

## لوحة الألوان

- **الأساسية**: أخضر رحّال (#00A651)
- **الثانوية**: أبيض، أسود، درجات الرمادي
- **التأكيد**: أحمر إماراتي (#EF3340) للتنبيهات والأخطاء

## الطباعة

- **العربية**: خط دبي / نوتو كوفي العربي
- **الإنجليزية**: مونتسيرات / سورس سانس برو#   S O C M I N T  
 