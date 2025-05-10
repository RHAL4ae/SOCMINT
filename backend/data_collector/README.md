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