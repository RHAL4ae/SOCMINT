import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ThemeService with ChangeNotifier {
  final SharedPreferences prefs;
  ThemeMode _currentMode = ThemeMode.system;

  ThemeService({required this.prefs}) {
    _loadTheme();
  }

  ThemeMode get themeMode => _currentMode;

  Future<void> initTheme() async {
    _loadTheme();
  }

  Future<void> _loadTheme() async {
    final savedMode = prefs.getString('theme_mode');
    if (savedMode != null) {
      _currentMode = ThemeMode.values.firstWhere(
        (mode) => mode.toString() == savedMode,
        orElse: () => ThemeMode.system,
      );
    }
    notifyListeners();
  }

  void toggleTheme() {
    _currentMode = _currentMode == ThemeMode.light
        ? ThemeMode.dark
        : ThemeMode.light;
    _saveTheme();
    notifyListeners();
  }

  Future<void> setThemeMode(ThemeMode mode) async {
    _currentMode = mode;
    await prefs.setString('theme_mode', mode.toString());
    notifyListeners();
  }

  Future<void> _saveTheme() async {
    await prefs.setString('theme_mode', _currentMode.toString());
  }
}
