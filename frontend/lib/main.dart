import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:provider/provider.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:theme_provider/theme_provider.dart' as theme_provider;
import 'package:shared_preferences/shared_preferences.dart';
import 'screens/dashboard/dashboard_screen.dart';
import 'assets/theme/theme_data.dart';
import 'services/theme_service.dart';
import 'services/language_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize secure storage
  final storage = FlutterSecureStorage();
  
  // Initialize shared preferences
  final prefs = await SharedPreferences.getInstance();
  
  // Initialize theme and language services
  final themeService = ThemeService(prefs: prefs);
  final languageService = LanguageService(storage: storage, prefs: prefs);
  
  // Initialize theme and language services
  await themeService.initTheme();
  await languageService.initLanguage();
  await languageService.initLanguage();
  
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => themeService),
        ChangeNotifierProvider(create: (_) => languageService),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer2<ThemeService, LanguageService>(
      builder: (context, themeService, languageService, child) {
        return theme_provider.ThemeProvider(
          saveThemesOnChange: true,
          loadThemeOnInit: true,
          themes: [
            theme_provider.AppTheme(
              id: 'light',
              data: AppTheme.lightTheme,
              description: 'Light theme',
            ),
            theme_provider.AppTheme(
              id: 'dark',
              data: AppTheme.darkTheme,
              description: 'Dark theme',
            ),
          ],
          child: MaterialApp(
            title: 'SOCMINT - RHAL',
            debugShowCheckedModeBanner: false,
            theme: AppTheme.lightTheme,
            darkTheme: AppTheme.darkTheme,
            themeMode: themeService.themeMode,
            localizationsDelegates: const [
              AppLocalizations.delegate,
              GlobalMaterialLocalizations.delegate,
              GlobalWidgetsLocalizations.delegate,
              GlobalCupertinoLocalizations.delegate,
            ],
            supportedLocales: const [
              Locale('ar', 'AE'),
              Locale('en', 'US'),
            ],
            locale: languageService.locale,
            home: const DashboardScreen(),
          ),
        );
      },
    );
  }
}

// Helper extension for RTL support
extension BuildContextExtensions on BuildContext {
  bool get isRTL => Directionality.of(this) == TextDirection.rtl;
}
