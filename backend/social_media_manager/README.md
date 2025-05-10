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