import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LanguageService with ChangeNotifier {
  final FlutterSecureStorage storage;
  final SharedPreferences prefs;
  Locale _locale = const Locale('ar', 'AE');

  LanguageService({required this.storage, required this.prefs}) {
    _loadLanguage();
  }

  Locale get locale => _locale;

  Future<void> initLanguage() async {
    _loadLanguage();
  }

  Future<void> _loadLanguage() async {
    final languageCode = await storage.read(key: 'language');
    if (languageCode != null) {
      _locale = Locale(languageCode, 'AE');
    } else {
      final savedLanguage = prefs.getString('language');
      if (savedLanguage != null) {
        _locale = Locale(savedLanguage, 'AE');
      }
    }
    notifyListeners();
  }

  Future<void> setLanguage(String languageCode) async {
    _locale = Locale(languageCode, 'AE');
    await storage.write(key: 'language', value: languageCode);
    await prefs.setString('language', languageCode);
    notifyListeners();
  }

  void toggleLanguage() {
    _locale = _locale.languageCode == 'ar'
        ? const Locale('en', 'US')
        : const Locale('ar', 'AE');
    _saveLanguage();
    notifyListeners();
  }

  void _saveLanguage() {
    prefs.setString('language', _locale.languageCode);
  }
}
