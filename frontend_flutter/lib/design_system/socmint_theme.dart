import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// SOCMINT Design System - Color Palette
/// 
/// This file implements the SOCMINT visual identity system color palette
/// and typography as defined in the design system documentation.
class SOCMINTColors {
  // Primary
  static const Color primary = Color(0xFF2E7D32); // Extracted green tone
  static const Color secondary = Color(0xFFFFFFFF);
  
  // Accent
  static const Color accent = Color(0xFFE31837); // Emirati flag red
  static const Color dark = Color(0xFF121212);
  
  // Grays
  static const Color lightGray = Color(0xFFF5F5F5);
  static const Color mediumGray = Color(0xFFCCCCCC);
  static const Color darkGray = Color(0xFF666666);
}

/// SOCMINT Design System - Typography
/// 
/// Text styles for both Arabic and English languages
class SOCMINTTextStyles {
  // Arabic Text Styles
  static TextStyle arabicH1 = GoogleFonts.notoKufiArabic(
    fontSize: 32,
    fontWeight: FontWeight.bold,
    height: 1.2,
  );
  
  static TextStyle arabicH2 = GoogleFonts.notoKufiArabic(
    fontSize: 24,
    fontWeight: FontWeight.bold,
    height: 1.3,
  );
  
  static TextStyle arabicH3 = GoogleFonts.notoKufiArabic(
    fontSize: 20,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  static TextStyle arabicH4 = GoogleFonts.notoKufiArabic(
    fontSize: 16,
    fontWeight: FontWeight.w600,
    height: 1.5,
  );
  
  static TextStyle arabicBody1 = GoogleFonts.notoKufiArabic(
    fontSize: 14,
    fontWeight: FontWeight.normal,
    height: 1.5,
  );
  
  static TextStyle arabicBody2 = GoogleFonts.notoKufiArabic(
    fontSize: 12,
    fontWeight: FontWeight.normal,
    height: 1.5,
  );
  
  // English Text Styles
  static TextStyle englishH1 = GoogleFonts.montserrat(
    fontSize: 32,
    fontWeight: FontWeight.bold,
    height: 1.2,
  );
  
  static TextStyle englishH2 = GoogleFonts.montserrat(
    fontSize: 24,
    fontWeight: FontWeight.bold,
    height: 1.3,
  );
  
  static TextStyle englishH3 = GoogleFonts.montserrat(
    fontSize: 20,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  static TextStyle englishH4 = GoogleFonts.montserrat(
    fontSize: 16,
    fontWeight: FontWeight.w600,
    height: 1.5,
  );
  
  static TextStyle englishBody1 = GoogleFonts.montserrat(
    fontSize: 14,
    fontWeight: FontWeight.normal,
    height: 1.5,
  );
  
  static TextStyle englishBody2 = GoogleFonts.montserrat(
    fontSize: 12,
    fontWeight: FontWeight.normal,
    height: 1.5,
  );
}

/// SOCMINT Theme Data
/// 
/// Complete theme implementation for the SOCMINT application
class SOCMINTTheme {
  // Light Theme
  static ThemeData lightTheme() {
    return ThemeData(
      primaryColor: SOCMINTColors.primary,
      colorScheme: ColorScheme.fromSeed(
        seedColor: SOCMINTColors.primary,
        primary: SOCMINTColors.primary,
        secondary: SOCMINTColors.secondary,
        error: SOCMINTColors.accent,
        brightness: Brightness.light,
      ),
      textTheme: TextTheme(
        headlineLarge: SOCMINTTextStyles.arabicH1,
        headlineMedium: SOCMINTTextStyles.arabicH2,
        headlineSmall: SOCMINTTextStyles.arabicH3,
        titleLarge: SOCMINTTextStyles.arabicH4,
        bodyLarge: SOCMINTTextStyles.arabicBody1,
        bodyMedium: SOCMINTTextStyles.arabicBody2,
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: SOCMINTColors.primary,
          foregroundColor: SOCMINTColors.secondary,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: SOCMINTColors.dark,
        elevation: 0,
        titleTextStyle: SOCMINTTextStyles.arabicH2,
      ),
      scaffoldBackgroundColor: SOCMINTColors.secondary,
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: SOCMINTColors.lightGray,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide.none,
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide.none,
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide(color: SOCMINTColors.primary),
        ),
      ),
      dialogTheme: DialogTheme(
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      bottomSheetTheme: BottomSheetThemeData(
        backgroundColor: SOCMINTColors.secondary,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(top: Radius.circular(12)),
        ),
      ),
      dividerTheme: DividerThemeData(
        color: SOCMINTColors.mediumGray,
        thickness: 1,
      ),
      snackBarTheme: SnackBarThemeData(
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8),
        ),
      ),
      bottomNavigationBarTheme: BottomNavigationBarThemeData(
        selectedItemColor: SOCMINTColors.primary,
        unselectedItemColor: SOCMINTColors.darkGray,
        showUnselectedLabels: true,
        type: BottomNavigationBarType.fixed,
      ),
      tabBarTheme: TabBarTheme(
        labelColor: SOCMINTColors.primary,
        unselectedLabelColor: SOCMINTColors.darkGray,
        indicator: BoxDecoration(
          borderRadius: BorderRadius.circular(8),
          color: SOCMINTColors.primary,
        ),
      ),
      drawerTheme: DrawerThemeData(
        backgroundColor: SOCMINTColors.dark,
      ),
      listTileTheme: ListTileThemeData(
        iconColor: SOCMINTColors.primary,
        textColor: SOCMINTColors.secondary,
      ),
      switchTheme: SwitchThemeData(
        thumbColor: WidgetStateProperty.all(SOCMINTColors.primary),
        trackColor: WidgetStateProperty.all(SOCMINTColors.mediumGray),
      ),
      checkboxTheme: CheckboxThemeData(
        fillColor: WidgetStateProperty.all(SOCMINTColors.primary),
        checkColor: WidgetStateProperty.all(SOCMINTColors.secondary),
      ),
      radioTheme: RadioThemeData(
        fillColor: WidgetStateProperty.all(SOCMINTColors.primary),
      ),
      sliderTheme: SliderThemeData(
        activeTrackColor: SOCMINTColors.primary,
        inactiveTrackColor: SOCMINTColors.mediumGray,
        thumbColor: SOCMINTColors.primary,
      ),
      progressIndicatorTheme: ProgressIndicatorThemeData(
        color: SOCMINTColors.primary,
      ),
    );
  }

  // Dark Theme
  static ThemeData darkTheme() {
    return ThemeData(
      primaryColor: SOCMINTColors.primary,
      scaffoldBackgroundColor: SOCMINTColors.dark,
      appBarTheme: AppBarTheme(
        backgroundColor: SOCMINTColors.dark,
        elevation: 0,
        titleTextStyle: SOCMINTTextStyles.arabicH2,
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
          backgroundColor: SOCMINTColors.primary,
          foregroundColor: SOCMINTColors.secondary,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          textStyle: SOCMINTTextStyles.englishBody1,
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: SOCMINTColors.primary,
          side: const BorderSide(color: SOCMINTColors.primary),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          textStyle: SOCMINTTextStyles.englishBody1,
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: TextButton.styleFrom(
          foregroundColor: SOCMINTColors.primary,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          textStyle: SOCMINTTextStyles.englishBody1,
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
          borderSide: const BorderSide(color: SOCMINTColors.primary),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: const BorderSide(color: SOCMINTColors.accent),
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
              return SOCMINTColors.primary;
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
        primary: SOCMINTColors.primary,
        secondary: SOCMINTColors.primary,
        error: SOCMINTColors.accent,
        surface: const Color(0xFF212121),
        onPrimary: SOCMINTColors.secondary,
        onSecondary: SOCMINTColors.secondary,
        onSurface: SOCMINTColors.secondary,
      ),
    );
  }
}