# SOCMINT Developer README 

# دليل مطور SOCMINT 

This technical README provides a comprehensive overview of the SOCMINT platform from a development and deployment perspective. It includes setup instructions, architectural layout, services, APIs, and integration flows.
هذا الملف التقني يقدم نظرة شاملة على منصة SOCMINT من منظور التطوير والنشر. يتضمن تعليمات الإعداد، التخطيط المعماري، الخدمات، واجهات البرمجة، وتدفقات التكامل.

---

## System Architecture

## البنية المعمارية للنظام

SOCMINT is a multi-service SaaS platform composed of:
تتكون منصة SOCMINT كخدمة SaaS متعددة الخدمات من:

* **Frontend**: Vue.js, Tailwind, i18n, UAE PASS OAuth
* **الواجهة الأمامية**: Vue.js, Tailwind, i18n, UAE PASS OAuth
* **Backend**: FastAPI microservices
* **الخلفية**: خدمات FastAPI المصغرة
* **Data Layer**: PostgreSQL, Elasticsearch, Neo4j
* **طبقة البيانات**: PostgreSQL، Elasticsearch، Neo4j
* **AI & Processing**: Kafka, Python ML services, LangChain, HuggingFace, DeepSeek
* **الذكاء الاصطناعي والمعالجة**: Kafka، خدمات ML بلغة بايثون، LangChain، HuggingFace، DeepSeek
* **Security & Identity**: JWT, UAE PASS OAuth2.0, blockchain logging, TOR routing
* **الأمن والهوية**: JWT، UAE PASS OAuth2.0، تسجيل بلوك تشين، توجيه عبر TOR

---

## Tech Stack

## التقنيات المستخدمة

| Component      | Stack                                             |
| -------------- | ------------------------------------------------- |
| Frontend | Vue.js, Tailwind, i18n, UAE PASS OAuth |
| Backend        | FastAPI, LangChain, Pydantic, Redis               |
| AI Services    | HuggingFace Transformers, DeepSeek R1, Google NLP |
| Databases      | PostgreSQL, Elasticsearch, Neo4j                  |
| Messaging      | Kafka (social & media ingestion)                  |
| Identity/Auth  | UAE PASS OAuth2.0, JWT                            |
| Scraping Layer | Playwright, Selenium, cURL over TOR               |
| Deployment     | Docker Compose, Traefik, `.env` files             |

| المكون                 | التقنية                                           |
| ---------------------- | ------------------------------------------------- |
| الواجهة الأمامية | Vue.js, Tailwind, i18n, UAE PASS OAuth |
| الخلفية                | FastAPI، LangChain، Pydantic، Redis               |
| خدمات الذكاء الاصطناعي | HuggingFace Transformers، DeepSeek R1، Google NLP |
| قواعد البيانات         | PostgreSQL، Elasticsearch، Neo4j                  |
| المراسلة               | Kafka (استخلاص وسائل التواصل والإعلام)            |
| الهوية/المصادقة        | UAE PASS OAuth2.0، JWT                            |
| طبقة الاستخلاص         | Playwright، Selenium، cURL عبر TOR                |
| النشر                  | Docker Compose، Traefik، ملفات `.env`             |

---

## Deployment Instructions

## تعليمات النشر

1. **Clone the repository**

   ```bash
   git clone https://github.com/rhal4ae/SOCMINT.git
   cd SOCMINT
   ```

2. **استنساخ المستودع**

   ```bash
   git clone https://github.com/rhal4ae/SOCMINT.git
   cd SOCMINT
   ```

3. **Create environment variables**

   ```bash
   cp .env.example .env
   ```

4. **إنشاء متغيرات البيئة**

   ```bash
   cp .env.example .env
   ```

5. **Launch with Docker Compose**

   ```bash
   docker-compose up -d
   ```

6. **تشغيل باستخدام Docker Compose**

   ```bash
   docker-compose up -d
   ```

7. **Access services**

   * Frontend: `http://localhost`
   * Backend: `http://localhost:8000`
   * Elasticsearch: `http://localhost:9200`
   * Neo4j: `http://localhost:7474`

8. **الوصول إلى الخدمات**

---

## Configuration Management

## إدارة التكوين

To enhance robustness and maintainability, the SOCMINT platform employs standardized configuration practices:
لتعزيز المتانة وقابلية الصيانة، تستخدم منصة SOCMINT ممارسات تكوين موحدة:

*   **Centralized Environment Variables**: The main `.env` file at the project root is the primary source for environment variables. Each backend microservice (`ai_analytics_service`, `social_media_manager`, `data_collector`) now consistently uses the `env_file: .env` directive in the `docker-compose.yml`. This ensures all services draw their configurations from this single, authoritative source when managed by Docker Compose.
*   **متغيرات البيئة المركزية**: ملف `.env` الرئيسي في جذر المشروع هو المصدر الأساسي لمتغيرات البيئة. تستخدم كل خدمة مصغرة في الخلفية (`ai_analytics_service`، `social_media_manager`، `data_collector`) الآن بشكل متسق التوجيه `env_file: .env` في ملف `docker-compose.yml`. هذا يضمن أن جميع الخدمات تستمد تكويناتها من هذا المصدر الموحد والموثوق عند إدارتها بواسطة Docker Compose.

*   **Service-Specific Configuration Validation**: Each backend microservice includes a `config.py` module responsible for:
    *   Loading its required environment variables.
    *   Validating critical configurations at startup.
    *   If critical configurations are missing or invalid, the service will log a detailed error message specifying the missing variables and will **fail to start**. This prevents services from running in an improperly configured state.
*   **التحقق من صحة التكوين الخاص بالخدمة**: تتضمن كل خدمة مصغرة في الخلفية وحدة `config.py` مسؤولة عن:
    *   تحميل متغيرات البيئة المطلوبة.
    *   التحقق من صحة التكوينات الحرجة عند بدء التشغيل.
    *   إذا كانت التكوينات الحرجة مفقودة أو غير صالحة، ستقوم الخدمة بتسجيل رسالة خطأ مفصلة تحدد المتغيرات المفقودة و **لن تبدأ التشغيل**. هذا يمنع الخدمات من العمل في حالة تكوين غير سليمة.

This approach ensures that services are always launched with the necessary configurations, improving overall system stability and making troubleshooting easier.
يضمن هذا النهج تشغيل الخدمات دائمًا بالتكوينات اللازمة، مما يحسن استقرار النظام بشكل عام ويسهل استكشاف الأخطاء وإصلاحها.

   * الواجهة الأمامية: `http://localhost`
   * الخلفية: `http://localhost:8000`
   * Elasticsearch: `http://localhost:9200`
   * Neo4j: `http://localhost:7474`

---

### Frontend Setup (Flutter)

### إعداد الواجهة الأمامية (Flutter)

1. `cd frontend_platform_all`
   - `cd frontend_platform_all` (الانتقال إلى مجلد الواجهة الأمامية)
2. `cp .env.example .env` (if needed)
   - `cp .env.example .env` (إذا لزم الأمر، انسخ ملف البيئة النموذجي)
3. `flutter pub get`
   - `flutter pub get` (للحصول على جميع الاعتماديات الخاصة بالمشروع)
4. `flutter run` (for mobile or desktop)
   - `flutter run` (لتشغيل التطبيق على الهاتف المحمول أو سطح المكتب)
5. `flutter run -d chrome` (for web development)
   - `flutter run -d chrome` (لتشغيل التطبيق كإصدار ويب في متصفح كروم)
6. `flutter build web` (for production web build)
   - `flutter build web` (لبناء إصدار الإنتاج من تطبيق الويب)
   - Output will be in `frontend_platform_all/build/web`
   - سيكون الناتج في المجلد `frontend_platform_all/build/web`
7. Deploy the contents of `build/web` to your web server (e.g., Nginx, Netlify, Vercel, or Docker)
   - انشر محتويات المجلد `build/web` على خادم الويب الخاص بك (مثل Nginx، Netlify، Vercel، أو Docker)

---


## API Endpoints

## نقاط النهاية (API)

| Endpoint              | Method | Description                  |
| --------------------- | ------ | ---------------------------- |
| `/auth/uaepass/login` | GET    | Redirect to UAE PASS login   |
| `/collect/twitter`    | POST   | Pull tweets from Twitter/X   |
| `/scrape/darkweb`     | GET    | Scrape dark web posts        |
| `/run-analysis`       | POST   | Execute NLP/ML pipelines     |
| `/generate-report`    | GET    | Generate intelligence report |
| `/verify/<report_id>` | GET    | Validate and audit a report  |
| `/api/media/alerts`   | GET    | Fetch sentiment alerts       |

| نقطة النهاية          | الطريقة | الوصف                                 |
| --------------------- | ------- | ------------------------------------- |
| `/auth/uaepass/login` | GET     | إعادة التوجيه إلى تسجيل دخول UAE PASS |
| `/collect/twitter`    | POST    | سحب التغريدات من Twitter/X            |
| `/scrape/darkweb`     | GET     | جمع منشورات الويب المظلم              |
| `/run-analysis`       | POST    | تنفيذ خطوط أنابيب NLP/ML              |
| `/generate-report`    | GET     | توليد تقرير استخباراتي                |
| `/verify/<report_id>` | GET     | التحقق ومراجعة تقرير                  |
| `/api/media/alerts`   | GET     | جلب تنبيهات المشاعر                   |

---

## Testing & Validation

## الاختبار والتحقق

* Use Postman or `curl` to exercise APIs.

* استخدم Postman أو `curl` لاختبار واجهات البرمجة.

* Validate role-based access: Admin, Analyst, Viewer.

* تحقق من الوصول حسب الدور: المسؤول، المحلل، المشاهد.

* Enable UAE PASS sandbox for SSO testing.

* فعّل بيئة UAE PASS التجريبية لاختبار الدخول الأحادي.

* Test TOR connectivity:

  ```bash
  curl --socks5-hostname localhost:9050 http://check.torproject.org
  ```

* اختبار توجيه TOR:

  ```bash
  curl --socks5-hostname localhost:9050 http://check.torproject.org
  ```

---

## KPIs & Analytics

## مؤشرات الأداء والتحليلات

* Integrated with GEM 2.1 indicators.

* متكامل مع مؤشرات GEM 2.1.

* Stored in Elasticsearch index `kpi_metrics_monthly`.

* مخزن في فهرس Elasticsearch باسم `kpi_metrics_monthly`.

* Displayed in `RahhalKPI.vue` dashboard.

* معروض في لوحة `RahhalKPI.vue`.

---

## Integrated Platforms

## المنصات المدمجة

* Facebook Graph API

* واجهة Facebook Graph API

* Twitter/X API v2

* واجهة Twitter/X API v2

* Telegram Bot API

* واجهة Telegram Bot API

* WhatsApp Business Cloud API

* واجهة WhatsApp Business Cloud API

* TikTok & Snap Map (web scraping)

* TikTok و Snap Map (جمع البيانات عبر الويب)

* Google Business Profile API

* واجهة Google Business Profile API

* Reddit JSON endpoints

* نقاط نهاية Reddit JSON

* Dark Web (via TOR scraping)
* **Postiz App (Social Media Management)**: Integrated for comprehensive social media scheduling, posting, and analytics. Future plans include migrating its frontend to Flutter for a unified experience. (See `postiz_app/README.md` for setup and usage)

---* الويب المظلم (عبر جمع البيانات عبر TOR)
* **تطبيق Postiz (إدارة وسائل التواصل الاجتماعي)**: مدمج لجدولة شاملة لوسائل التواصل الاجتماعي والنشر والتحليلات. تشمل الخطط المستقبلية ترحيل واجهته الأمامية إلى Flutter لتجربة موحدة. (راجع `postiz_app/README.md` للإعداد والاستخدام)

---

## Security Considerations

## اعتبارات أمنية

* HTTPS enforced via Traefik.

* تفعيل HTTPS عبر Traefik.

* Blockchain logging of report trails.

* تسجيل سلاسل التقارير عبر البلوك تشين.

* Verifiable credentials via DID.

* بيانات اعتماد يمكن التحقق منها عبر DID.

* TOR routing with Dockerized SOCKS5.

* توجيه TOR باستخدام SOCKS5 في حاوية Docker.

* JWT session management.

* إدارة الجلسات باستخدام JWT.

---

## Project Structure

## هيكل المشروع

The repository is structured as follows:
يتم تنظيم المستودع على النحو التالي:

```bash
Project/
├── backend/             # FastAPI microservices
├── frontend_platform_all/ # Unified Flutter frontend (Web & Mobile)
├── Promots/             # Prompt templates
├── ...
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   └── services/
├── frontend_platform_all/ # Unified Flutter frontend
│   ├── lib/               # Main application code
│   ├── assets/            # Static assets
│   └── web/               # Web-specific files
├── docker-compose.yml
├── .env.example
└── nginx/ traefik/
```

---

## 🤖 AI Agents

## 🤖 وكلاء الذكاء الاصطناعي

Modular LLM agents for:
وكلاء LLM modular من أجل:

* Entity classification

* تصنيف الكيانات

* Financial anomaly detection

* كشف الشذوذ المالي

* Risk scoring (DeepSeek R1)

* تقييم المخاطر (DeepSeek R1)

* NLP-based media profiling

* إنشاء ملفات تعريف الإعلام باستخدام NLP

---

## 🤝 Contribution Guidelines

## 🤝 إرشادات المساهمة

1. Create descriptive branch names: `feature/...`, `bugfix/...`.

2. أنشئ أسماء فروع وصفية: `feature/...`، `bugfix/...`.

3. Submit clear commit messages and PR descriptions.

4. قدم رسائل commit واضحة ووصفًا للـ PR.

5. Follow PEP8 and ESLint conventions.

6. اتبع قواعد PEP8 و ESLint.

7. Update `CHANGELOG.md` for major changes.

8. حدّث `CHANGELOG.md` للتغييرات الرئيسية.

9. Maintain `.env.example` with template values.

10. حافظ على `.env.example` مع القيم النموذجية.

---

**Maintained by**: Rami Kamel | SOCMINT Architect
**Location**: Ajman, UAE 🇦🇪

**تمت الصيانة بواسطة**: رامي كامل | مهندس منصة SOCMINT
**الموقع**: عجمان، الإمارات 🇦🇪
