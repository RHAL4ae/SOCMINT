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
- **الإنجليزية**: مونتسيرات / سورس سانس برو