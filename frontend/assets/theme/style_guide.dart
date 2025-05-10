import 'package:flutter/material.dart';

class StyleGuide {
  // Color Tokens
  static const Map<String, Color> colors = {
    'primary': Color(0xFF2E7D32),
    'accent': Color(0xFFD32F2F),
    'secondary': Color(0xFFFFFFFF),
    'background': Color(0xFF000000),
    'text': Color(0xFF000000),
    'text-light': Color(0xFFE0E0E0),
    'border': Color(0xFFE0E0E0),
    'shadow': Color(0x1F000000),
  };

  // Typography Tokens
  static const Map<String, TextStyle> typography = {
    'heading-1': TextStyle(
      fontFamily: 'Dubai',
      fontSize: 32,
      fontWeight: FontWeight.w700,
      height: 1.2,
    ),
    'heading-2': TextStyle(
      fontFamily: 'Dubai',
      fontSize: 24,
      fontWeight: FontWeight.w600,
      height: 1.2,
    ),
    'heading-3': TextStyle(
      fontFamily: 'Dubai',
      fontSize: 20,
      fontWeight: FontWeight.w600,
      height: 1.2,
    ),
    'body-large': TextStyle(
      fontFamily: 'Dubai',
      fontSize: 16,
      fontWeight: FontWeight.w400,
      height: 1.5,
    ),
    'body-medium': TextStyle(
      fontFamily: 'Dubai',
      fontSize: 14,
      fontWeight: FontWeight.w400,
      height: 1.5,
    ),
    'body-small': TextStyle(
      fontFamily: 'Dubai',
      fontSize: 12,
      fontWeight: FontWeight.w400,
      height: 1.5,
    ),
  };

  // Spacing Tokens
  static const Map<String, double> spacing = {
    'x-small': 4.0,
    'small': 8.0,
    'medium': 16.0,
    'large': 24.0,
    'x-large': 32.0,
  };

  // Border Radius Tokens
  static const Map<String, double> borderRadius = {
    'small': 4.0,
    'medium': 8.0,
    'large': 12.0,
  };

  // Shadow Tokens
  static const Map<String, BoxShadow> shadows = {
    'small': BoxShadow(
      color: Color(0x1F000000),
      blurRadius: 4,
      offset: Offset(0, 2),
    ),
    'medium': BoxShadow(
      color: Color(0x1F000000),
      blurRadius: 8,
      offset: Offset(0, 4),
    ),
    'large': BoxShadow(
      color: Color(0x1F000000),
      blurRadius: 12,
      offset: Offset(0, 6),
    ),
  };

  // Component Styles
  static const Map<String, dynamic> components = {
    'button': {
      'padding': EdgeInsets.symmetric(horizontal: 24, vertical: 12),
      'borderRadius': 8.0,
      'fontSize': 16,
      'fontWeight': FontWeight.w600,
    },
    'card': {
      'padding': EdgeInsets.all(16),
      'borderRadius': 12.0,
      'elevation': 2,
    },
    'input': {
      'padding': EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      'borderRadius': 8.0,
      'fontSize': 16,
    },
    'table': {
      'cellPadding': EdgeInsets.all(8),
      'headerHeight': 48,
      'rowHeight': 40,
    },
  };

  // Layout Grid
  static const Map<String, dynamic> grid = {
    'columns': 12,
    'gutter': 16,
    'breakpoints': {
      'mobile': 320,
      'tablet': 768,
      'desktop': 1024,
    },
  };

  // Animation Tokens
  static const Map<String, dynamic> animations = {
    'duration': Duration(milliseconds: 200),
    'curve': Curves.easeInOut,
    'fade': {
      'duration': Duration(milliseconds: 300),
      'curve': Curves.easeInOut,
    },
    'scale': {
      'duration': Duration(milliseconds: 200),
      'curve': Curves.easeOut,
    },
  };

  // Accessibility
  static const Map<String, dynamic> accessibility = {
    'textContrast': 4.5,
    'minFontSize': 16,
    'minTouchTarget': 44,
    'colorBlindModes': [
      'Protanopia',
      'Deuteranopia',
      'Tritanopia',
    ],
    'keyboardNavigation': true,
    'screenReaderSupport': true,
  };

  // RTL Support
  static const Map<String, dynamic> rtl = {
    'textDirection': TextDirection.rtl,
    'layoutDirection': TextDirection.rtl,
    'paddingAdjustments': true,
    'iconPositioning': true,
  };

  // Brand Assets
  static const Map<String, dynamic> assets = {
    'logo': {
      'primary': 'assets/images/logo/logo_primary.png',
      'white': 'assets/images/logo/logo_white.png',
      'black': 'assets/images/logo/logo_black.png',
      'favicon': 'assets/images/logo/favicon.png',
      'minSize': 128,
      'aspectRatio': 1,
    },
    'icons': {
      'format': 'SVG',
      'sizes': [24, 32, 48],
      'colorModes': ['primary', 'secondary', 'accent'],
    },
  };

  // Documentation
  static const Map<String, dynamic> documentation = {
    'version': '1.0.0',
    'lastUpdated': '2025-05-10',
    'authors': ['Design Team'],
    'changelog': [
      {
        'date': '2025-05-10',
        'version': '1.0.0',
        'changes': [
          'Initial release',
          'Added color system',
          'Added typography',
          'Added components',
        ],
      },
    ],
  };
}
