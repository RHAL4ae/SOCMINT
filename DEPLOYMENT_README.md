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