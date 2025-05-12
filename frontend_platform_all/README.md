# SOCMINT Unified Frontend (frontend_platform_all)

This project combines the Flutter-based frontend (formerly `frontend_flutter`) and potentially other frontend components into a single, unified platform. This directory now serves as the primary frontend for the SOCMINT application.

## دليل الواجهة الأمامية الموحدة لـ SOCMINT (frontend_platform_all)

يجمع هذا المشروع بين الواجهة الأمامية المستندة إلى Flutter (التي كانت سابقًا في `frontend_flutter`) وربما مكونات الواجهة الأمامية الأخرى في منصة واحدة موحدة. يعمل هذا الدليل الآن كالواجهة الأمامية الرئيسية لتطبيق SOCMINT.

## Project Information / معلومات المشروع

This is a Flutter project, primarily based on the original `frontend_flutter` codebase.
هذا مشروع فلاتر، يعتمد بشكل أساسي على قاعدة بيانات `frontend_flutter` الأصلية.

## Setup and Deployment / الإعداد والنشر

### Frontend Setup (Flutter) / إعداد الواجهة الأمامية (Flutter)

1.  Navigate to this directory: `cd frontend_platform_all`
    انتقل إلى هذا الدليل: `cd frontend_platform_all`
2.  If an example environment file exists (e.g., `.env.example`), copy it to `.env` and customize as needed: `cp .env.example .env` (if needed)
    إذا كان ملف بيئة مثال موجودًا (على سبيل المثال، `.env.example`)، قم بنسخه إلى `.env` وقم بتخصيصه حسب الحاجة: `cp .env.example .env` (إذا لزم الأمر)
3.  Get Flutter packages: `flutter pub get`
    احصل على حزم فلاتر: `flutter pub get`
4.  Run the application (for mobile or desktop): `flutter run`
    قم بتشغيل التطبيق (للجوال أو سطح المكتب): `flutter run`
5.  Run the application for web development: `flutter run -d chrome`
    قم بتشغيل التطبيق لتطوير الويب: `flutter run -d chrome`
6.  Build for production (web): `flutter build web`
    إنشاء نسخة الإنتاج (للوeb): `flutter build web`
    - Output will be in `frontend_platform_all/build/web`
    - سيكون الناتج في `frontend_platform_all/build/web`
7.  Deploy the contents of `build/web` to your web server (e.g., Nginx, Netlify, Vercel, or Docker).
    انشر محتويات `build/web` على خادم الويب الخاص بك (مثل Nginx، Netlify، Vercel، أو Docker).

---
(Further details will be added as the project evolves / سيتم إضافة المزيد من التفاصيل مع تطور المشروع)
