import 'package:flutter/material.dart';

/// SOCMINT Design System - Color Palette
/// 
/// This file implements the SOCMINT visual identity system color palette
/// and typography as defined in the design system documentation.
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

/// SOCMINT Design System - Typography
/// 
/// Text styles for both Arabic and English languages
class SOCMINTTextStyles {
  // Arabic Text Styles
  static const TextStyle arabicH1 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 32,
    fontWeight: FontWeight.w700,
    height: 1.2,
  );
  
  static const TextStyle arabicH2 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 24,
    fontWeight: FontWeight.w700,
    height: 1.3,
  );
  
  static const TextStyle arabicH3 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 20,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  static const TextStyle arabicH4 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 18,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  static const TextStyle arabicBody1 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 16,
    fontWeight: FontWeight.w400,
    height: 1.5,
  );
  
  static const TextStyle arabicBody2 = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 14,
    fontWeight: FontWeight.w400,
    height: 1.5,
  );
  
  static const TextStyle arabicCaption = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 12,
    fontWeight: FontWeight.w400,
    height: 1.4,
  );
  
  static const TextStyle arabicButton = TextStyle(
    fontFamily: 'Dubai',
    fontSize: 16,
    fontWeight: FontWeight.w600,
    height: 1.2,
  );
  
  // English Text Styles
  static const TextStyle englishH1 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 32,
    fontWeight: FontWeight.w700,
    height: 1.2,
  );
  
  static const TextStyle englishH2 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 24,
    fontWeight: FontWeight.w700,
    height: 1.3,
  );
  
  static const TextStyle englishH3 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 20,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  static const TextStyle englishH4 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 18,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  static const TextStyle englishBody1 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 16,
    fontWeight: FontWeight.w400,
    height: 1.5,
  );
  
  static const TextStyle englishBody2 = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 14,
    fontWeight: FontWeight.w400,
    height: 1.5,
  );
  
  static const TextStyle englishCaption = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 12,
    fontWeight: FontWeight.w400,
    height: 1.4,
  );
  
  static const TextStyle englishButton = TextStyle(
    fontFamily: 'Montserrat',
    fontSize: 16,
    fontWeight: FontWeight.w600,
    height: 1.2,
  );
}

/// SOCMINT Theme Data
/// 
/// Complete theme implementation for the SOCMINT application
class SOCMINTTheme {
  // Light Theme
  static ThemeData lightTheme() {
    return ThemeData(
      primaryColor: SOCMINTColors.rhalGreen,
      scaffoldBackgroundColor: SOCMINTColors.lightGray,
      appBarTheme: const AppBarTheme(
        backgroundColor: SOCMINTColors.white,
        foregroundColor: SOCMINTColors.rhalDark,
        elevation: 1,
      ),
      cardTheme: const CardTheme(
        color: SOCMINTColors.white,
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.all(Radius.circular(12)),
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: SOCMINTColors.rhalGreen,
          foregroundColor: SOCMINTColors.white,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          textStyle: SOCMINTTextStyles.englishButton,
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: SOCMINTColors.rhalGreen,
          side: const BorderSide(color: SOCMINTColors.rhalGreen),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          textStyle: SOCMINTTextStyles.englishButton,
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: TextButton.styleFrom(
          foregroundColor: SOCMINTColors.rhalGreen,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          textStyle: SOCMINTTextStyles.englishButton,
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: SOCMINTColors.white,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.mediumGray),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.mediumGray),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.rhalGreen),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.uaeRed),
        ),
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      ),
      checkboxTheme: CheckboxThemeData(
        fillColor: WidgetStateProperty.resolveWith<Color>(
          (Set<WidgetState> states) {
            if (states.contains(WidgetState.disabled)) {
              return SOCMINTColors.mediumGray;
            }
            if (states.contains(WidgetState.selected)) {
              return SOCMINTColors.rhalGreen;
            }
            return SOCMINTColors.white;
          },
        ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(4)),
      ),
      dividerTheme: const DividerThemeData(
        color: SOCMINTColors.lightGray,
        thickness: 1,
        space: 1,
      ),
      colorScheme: ColorScheme.light(
        primary: SOCMINTColors.rhalGreen,
        secondary: SOCMINTColors.rhalGreen,
        error: SOCMINTColors.uaeRed,
        surface: SOCMINTColors.white,
        onPrimary: SOCMINTColors.white,
        onSecondary: SOCMINTColors.white,
        onError: SOCMINTColors.white,
        onSurface: SOCMINTColors.rhalDark,
      ),
    );
  }

  // Dark Theme
  static ThemeData darkTheme() {
    return ThemeData(
      primaryColor: SOCMINTColors.rhalGreen,
      scaffoldBackgroundColor: SOCMINTColors.rhalDark,
      appBarTheme: const AppBarTheme(
        backgroundColor: Color(0xFF212121),
        foregroundColor: SOCMINTColors.white,
        elevation: 1,
      ),
      cardTheme: const CardTheme(
        color: Color(0xFF212121),
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.all(Radius.circular(12)),
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: SOCMINTColors.rhalGreen,
          foregroundColor: SOCMINTColors.white,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          textStyle: SOCMINTTextStyles.englishButton,
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: SOCMINTColors.rhalGreen,
          side: const BorderSide(color: SOCMINTColors.rhalGreen),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          textStyle: SOCMINTTextStyles.englishButton,
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: TextButton.styleFrom(
          foregroundColor: SOCMINTColors.rhalGreen,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          textStyle: SOCMINTTextStyles.englishButton,
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: const Color(0xFF212121),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.darkGray),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.darkGray),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.rhalGreen),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.uaeRed),
        ),
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      ),
      checkboxTheme: CheckboxThemeData(
        fillColor: WidgetStateProperty.resolveWith<Color>(
          (Set<WidgetState> states) {
            if (states.contains(WidgetState.disabled)) {
              return SOCMINTColors.darkGray;
            }
            if (states.contains(WidgetState.selected)) {
              return SOCMINTColors.rhalGreen;
            }
            return const Color(0xFF212121);
          },
        ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(4)),
      ),
      dividerTheme: const DividerThemeData(
        color: Color(0xFF333333),
        thickness: 1,
        space: 1,
      ),
      colorScheme: ColorScheme.dark(
        primary: SOCMINTColors.rhalGreen,
        secondary: SOCMINTColors.rhalGreen,
        error: SOCMINTColors.uaeRed,
        surface: const Color(0xFF212121),
        onPrimary: SOCMINTColors.white,
        onSecondary: SOCMINTColors.white,
        onError: SOCMINTColors.white,
        onSurface: SOCMINTColors.white,
      ),
    );
  }
}