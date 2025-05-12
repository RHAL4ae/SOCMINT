import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class Logo {
  static const String primary = 'assets/images/logo/logo_primary.png';
  static const String white = 'assets/images/logo/logo_white.png';
  static const String black = 'assets/images/logo/logo_black.png';
  static const String favicon = 'assets/images/logo/favicon.png';

  Widget getPrimary(BuildContext context) {
    return Image.asset(
      primary,
      height: 40,
      width: 120,
    );
  }

  static Widget getWhite({
    double? width,
    double? height,
    BoxFit fit = BoxFit.contain,
  }) {
    return Image.asset(
      white,
      width: width,
      height: height,
      fit: fit,
    );
  }

  static Widget getBlack({
    double? width,
    double? height,
    BoxFit fit = BoxFit.contain,
  }) {
    return Image.asset(
      black,
      width: width,
      height: height,
      fit: fit,
    );
  }

  static Widget getFavicon({
    double? width,
    double? height,
    BoxFit fit = BoxFit.contain,
  }) {
    return Image.asset(
      favicon,
      width: width,
      height: height,
      fit: fit,
    );
  }

  static const Map<String, Map<String, dynamic>> usageGuidelines = {
    'primary': {
      'description': 'Primary logo for light backgrounds',
      'color': 'White',
      'background': 'Black/Dark',
      'minSize': 128,
      'clearSpace': 1,
    },
    'white': {
      'description': 'White logo for dark backgrounds',
      'color': 'White',
      'background': 'Black/Dark',
      'minSize': 128,
      'clearSpace': 1,
    },
    'black': {
      'description': 'Black logo for light backgrounds',
      'color': 'Black',
      'background': 'White/Light',
      'minSize': 128,
      'clearSpace': 1,
    },
    'favicon': {
      'description': 'Favicon for web and app',
      'color': 'Primary Green',
      'background': 'Transparent',
      'sizes': [512, 192, 48],
    },
  };

  static const Map<String, Map<String, dynamic>> technicalSpecs = {
    'primary': {
      'format': 'PNG',
      'colors': ['White', 'Primary Green'],
      'dimensions': '128x128',
      'requirements': [
        'Preserve green bar above "رحّال"',
        'Maintain aspect ratio',
        'No distortion',
        'No recoloring',
        'No inversion'
      ],
    },
    'white': {
      'format': 'PNG',
      'colors': ['White', 'Primary Green'],
      'dimensions': '128x128',
      'requirements': [
        'Preserve green bar above "رحّال"',
        'Maintain aspect ratio',
        'No distortion',
        'No recoloring',
        'No inversion'
      ],
    },
    'black': {
      'format': 'PNG',
      'colors': ['Black', 'Primary Green'],
      'dimensions': '128x128',
      'requirements': [
        'Preserve green bar above "رحّال"',
        'Maintain aspect ratio',
        'No distortion',
        'No recoloring',
        'No inversion'
      ],
    },
    'favicon': {
      'format': 'PNG',
      'colors': ['Primary Green'],
      'dimensions': '512x512',
      'requirements': [
        'Square format',
        'Transparent background',
        'Multiple sizes (512x512, 192x192, 48x48)',
        'Export as SVG and PNG'
      ],
    },
  };
}
