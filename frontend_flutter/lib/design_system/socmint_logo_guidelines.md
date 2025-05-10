# RHAL Logo Guidelines

## Overview

The RHAL logo ("رحّال") is the primary visual identifier for the SOCMINT platform. This document provides comprehensive guidelines for its proper usage across all applications, ensuring brand consistency and recognition.

## Logo Elements

### Primary Components

1. **Arabic Text**: The word "رحّال" in white (on dark backgrounds) or black (on light backgrounds)
2. **Green Bar**: The distinctive green bar above the text in RHAL Green (#00A651)

### Logo Variants

1. **Primary Logo**: White text on black background with green bar
2. **Reversed Logo**: Black text on white background with green bar
3. **Monochrome White**: All white elements (for dark backgrounds)
4. **Monochrome Black**: All black elements (for light backgrounds)

## Clear Space

Maintain a minimum clear space around the logo equal to the height of the letter "ر" in the logo. This space must be free from any other graphic elements, text, or page edges.

```
┌───────────────────────────┐
│                           │
│     [Clear Space Area]    │
│   ┌───────────────────┐   │
│   │   [Green Bar]     │   │
│   │   رحّال           │   │
│   └───────────────────┘   │
│                           │
└───────────────────────────┘
```

## Size Requirements

- **Minimum Digital Size**: 24px height
- **Minimum Print Size**: 10mm height
- **Favicon/App Icon**: Use the square version at 512×512, 192×192, 48×48, 32×32, 16×16 sizes

## Color Specifications

- **RHAL Green**: #00A651 / RGB(0, 166, 81)
- **Black**: #1A1A1A / RGB(26, 26, 26)
- **White**: #FFFFFF / RGB(255, 255, 255)

## Incorrect Usage

DO NOT:
- Distort or stretch the logo
- Change the colors of the logo elements
- Rotate or flip the logo
- Remove the green bar
- Add effects (shadows, glows, etc.) to the logo
- Place the logo on busy backgrounds that reduce visibility
- Enclose the logo in shapes that constrain its clear space

## Placement

### Digital Applications

- **Website Header**: Top left corner
- **Mobile App**: Center of splash screen, top left of main interface
- **Dashboard**: Top left of navigation bar
- **Social Media Profile**: Use the square version as profile picture

### Print Applications

- **Business Cards**: Centered at top
- **Letterhead**: Top left corner
- **Reports**: Cover page (centered), interior pages (top left, smaller size)

## File Formats

- **Vector**: SVG (preferred for digital), AI, EPS (for print)
- **Raster**: PNG with transparency (for digital), JPEG (for print)

## Logo with Tagline

When using the logo with the tagline "عجمان للتقنيات المتقدمة":

1. Place the tagline below the logo
2. Maintain a distance equal to half the height of the logo
3. Center-align the tagline with the logo
4. Use a font size approximately 50% of the logo height

## Logo in Different Languages

The primary logo is in Arabic ("رحّال"). When used in predominantly English contexts:

1. Maintain the Arabic logo
2. If needed, add "RHAL" in English using Montserrat Bold font below the Arabic logo
3. The English text should be 70% of the Arabic text size

## Digital Implementation

### SVG Code Example

```svg
<svg width="200" height="80" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
  <!-- Green Bar -->
  <rect x="40" y="20" width="120" height="8" fill="#00A651" />
  
  <!-- Arabic Text "رحّال" -->
  <text x="100" y="60" font-family="Dubai, 'Noto Kufi Arabic', sans-serif" font-size="32" font-weight="bold" fill="#FFFFFF" text-anchor="middle" direction="rtl" unicode-bidi="bidi-override">رحّال</text>
</svg>
```

### CSS Implementation

```css
.rhal-logo {
  position: relative;
  font-family: 'Dubai', 'Noto Kufi Arabic', sans-serif;
  font-weight: bold;
  font-size: 32px;
  color: #FFFFFF;
  text-align: center;
  direction: rtl;
  padding-top: 16px;
  width: 120px;
}

.rhal-logo::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 8px;
  background-color: #00A651;
}
```

## Flutter Implementation

```dart
class RHALLogo extends StatelessWidget {
  final double height;
  final bool isReversed;
  final bool isMonochrome;
  
  const RHALLogo({
    Key? key,
    this.height = 40,
    this.isReversed = false,
    this.isMonochrome = false,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    final Color textColor = isMonochrome
        ? (Theme.of(context).brightness == Brightness.dark ? Colors.white : Colors.black)
        : (isReversed ? Colors.black : Colors.white);
    
    final Color barColor = isMonochrome
        ? textColor
        : SOCMINTColors.rhalGreen;
    
    final Color backgroundColor = isReversed ? Colors.white : Colors.black;
    
    return Container(
      height: height,
      padding: EdgeInsets.symmetric(horizontal: height * 0.5),
      color: backgroundColor,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Container(
            height: height * 0.2,
            color: barColor,
          ),
          SizedBox(height: height * 0.1),
          Text(
            'رحّال',
            style: TextStyle(
              fontFamily: 'Dubai',
              fontSize: height * 0.6,
              fontWeight: FontWeight.bold,
              color: textColor,
            ),
            textDirection: TextDirection.rtl,
          ),
        ],
      ),
    );
  }
}
```

---

# إرشادات شعار رحّال

## نظرة عامة

شعار رحّال هو المعرّف البصري الأساسي لمنصة SOCMINT. توفر هذه الوثيقة إرشادات شاملة للاستخدام السليم للشعار عبر جميع التطبيقات، مما يضمن اتساق العلامة التجارية والتعرف عليها.

## عناصر الشعار

### المكونات الأساسية

1. **النص العربي**: كلمة "رحّال" باللون الأبيض (على خلفيات داكنة) أو الأسود (على خلفيات فاتحة)
2. **الشريط الأخضر**: الشريط الأخضر المميز فوق النص بلون رحّال الأخضر (#00A651)

## المساحة الخالية

يجب الحفاظ على مساحة خالية حول الشعار تساوي ارتفاع حرف "ر" في الشعار. يجب أن تكون هذه المساحة خالية من أي عناصر رسومية أخرى أو نص أو حواف الصفحة.

## متطلبات الحجم

- **الحد الأدنى للحجم الرقمي**: ارتفاع 24 بكسل
- **الحد الأدنى لحجم الطباعة**: ارتفاع 10 مم

## مواصفات الألوان

- **أخضر رحّال**: #00A651 / RGB(0, 166, 81)
- **أسود**: #1A1A1A / RGB(26, 26, 26)
- **أبيض**: #FFFFFF / RGB(255, 255, 255)

## الاستخدام غير الصحيح

لا تقم بـ:
- تشويه أو تمديد الشعار
- تغيير ألوان عناصر الشعار
- تدوير أو قلب الشعار
- إزالة الشريط الأخضر
- إضافة تأثيرات (ظلال، توهج، إلخ) إلى الشعار
- وضع الشعار على خلفيات مزدحمة تقلل من الرؤية
- إحاطة الشعار بأشكال تقيد مساحته الخالية

## التنفيذ الرقمي

يجب استخدام الشعار بشكل متسق عبر جميع المنصات الرقمية، مع الحفاظ على نسب وألوان الشعار الأصلية. استخدم دائمًا ملفات الشعار الرسمية ولا تحاول إعادة إنشاء الشعار.