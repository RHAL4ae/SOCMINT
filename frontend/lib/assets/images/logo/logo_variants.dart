import 'package:flutter/material.dart';

class Logo {
  static const String primary = 'assets/images/logo/logo_primary.png';
  static const String white = 'assets/images/logo/logo_white.png';
  static const String black = 'assets/images/logo/logo_black.png';
  static const String icon = 'assets/images/logo/favicon.png';

  static Widget primaryLogo({
    double? width,
    double? height,
    Color? color,
  }) {
    return Image.asset(
      primary,
      width: width,
      height: height,
      color: color,
    );
  }

  static Widget whiteLogo({
    double? width,
    double? height,
  }) {
    return Image.asset(
      white,
      width: width,
      height: height,
    );
  }

  static Widget blackLogo({
    double? width,
    double? height,
  }) {
    return Image.asset(
      black,
      width: width,
      height: height,
    );
  }

  static Widget favicon({
    double? width,
    double? height,
  }) {
    return Image.asset(
      icon,
      width: width,
      height: height,
    );
  }
}
