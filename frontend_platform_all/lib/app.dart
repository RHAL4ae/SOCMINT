import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:google_fonts/google_fonts.dart';
import 'localization/intl_localizations.dart';
import 'config/app_routes.dart';

class SocmintDashboardApp extends StatelessWidget {
  const SocmintDashboardApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SOCMINT Dashboard',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: GoogleFonts.notoKufiArabic().fontFamily,
        brightness: Brightness.light,
        primarySwatch: Colors.blue,
      ),
      darkTheme: ThemeData(
        fontFamily: GoogleFonts.notoKufiArabic().fontFamily,
        brightness: Brightness.dark,
        primarySwatch: Colors.blue,
      ),
      localizationsDelegates: const [
        SocmintLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('en'),
        Locale('ar'),
        Locale('fa'),
        Locale('ru'),
      ],
      localeResolutionCallback: (locale, supportedLocales) {
        if (locale == null) return supportedLocales.first;
        for (var supportedLocale in supportedLocales) {
          if (supportedLocale.languageCode == locale.languageCode) {
            return supportedLocale;
          }
        }
        return supportedLocales.first;
      },
      initialRoute: AppRoutes.login,
      routes: AppRoutes.routes,
    );
  }
}