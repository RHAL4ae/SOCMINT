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