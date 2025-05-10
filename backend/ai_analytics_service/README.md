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