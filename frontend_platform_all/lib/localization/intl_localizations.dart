import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class SocmintLocalizations {
  final Locale locale;
  late Map<String, String> _localizedStrings;

  SocmintLocalizations(this.locale);

  static const LocalizationsDelegate<SocmintLocalizations> delegate = _SocmintLocalizationsDelegate();

  static SocmintLocalizations? of(BuildContext context) {
    return Localizations.of<SocmintLocalizations>(context, SocmintLocalizations);
  }

  Future<bool> load() async {
    String jsonString = await rootBundle.loadString('lib/localization/intl_${locale.languageCode}.arb');
    Map<String, dynamic> jsonMap = json.decode(jsonString);
    _localizedStrings = jsonMap.map((key, value) => MapEntry(key, value.toString()));
    return true;
  }

  String translate(String key) {
    return _localizedStrings[key] ?? key;
  }
}

class _SocmintLocalizationsDelegate extends LocalizationsDelegate<SocmintLocalizations> {
  const _SocmintLocalizationsDelegate();

  @override
  bool isSupported(Locale locale) => ['en', 'ar', 'fa', 'ru'].contains(locale.languageCode);

  @override
  Future<SocmintLocalizations> load(Locale locale) async {
    SocmintLocalizations localizations = SocmintLocalizations(locale);
    await localizations.load();
    return localizations;
  }

  @override
  bool shouldReload(_SocmintLocalizationsDelegate old) => false;
}