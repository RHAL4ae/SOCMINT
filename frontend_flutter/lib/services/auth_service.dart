import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'api_service.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:logger/logger.dart';
// Only import dart:html for web
// ignore: avoid_web_libraries_in_flutter
import 'dart:html' as html;
import 'jwt_utils.dart';

class AuthService {
  static final FlutterSecureStorage _storage = const FlutterSecureStorage();

  static Future<bool> login(String username, String password) async {
    try {
      final response = await ApiService.request(
        '/auth/login',
        method: 'POST',
        data: {'username': username, 'password': password},
      );
      final token = response.data['token'];
      if (token != null) {
        await _storage.write(key: 'jwt_token', value: token);
        return true;
      }
      return false;
    } on DioException {
      return false;
    }
  }

  static Future<void> logout() async {
    await _storage.delete(key: 'jwt_token');
  }

  // UAE PASS OAuth2 login integration
  static Future<bool> loginWithUAEPASS() async {
    try {
      // Get the backend URL from ApiService
      final baseUrl = ApiService.baseUrl;
      
      // Redirect to UAE PASS login endpoint
      final uaePassLoginUrl = '$baseUrl/auth/uaepass/login';
      
      // Open the UAE PASS login URL in a web view or browser
      // This will redirect to UAE PASS, then back to our callback URL
      // For Flutter Web, we can use window.location.href
      // For mobile, we would use url_launcher or in-app webview
      if (kIsWeb) {
        // Web implementation
        html.window.location.href = uaePassLoginUrl;
        return true; // This won't actually return as page will redirect
      } else {
        // Mobile implementation using url_launcher
        try {
          // Uncomment the following lines if url_launcher is added to pubspec.yaml
          // import 'package:url_launcher/url_launcher.dart';
          // if (await canLaunch(uaePassLoginUrl)) {
          //   await launch(uaePassLoginUrl, forceSafariVC: true, forceWebView: true);
          //   return true;
          // } else {
          //   throw Exception('Could not launch UAE PASS login URL');
          // }
          throw Exception('Mobile implementation not available yet. Please add url_launcher package.');
        } catch (e) {
          Logger().e('UAE PASS mobile login error: $e');
          return false;
        }
      }
    } catch (e) {
      Logger().e('UAE PASS login error: $e');
      return false;
    }
  }
  
  // Process UAE PASS callback and extract JWT
  static Future<bool> processUAEPassCallback(String url) async {
    try {
      // Extract JWT from the callback URL or response
      if (url.contains('jwt=')) {
        final jwt = Uri.parse(url).queryParameters['jwt'];
        if (jwt != null) {
          await _storage.write(key: 'jwt_token', value: jwt);
          return true;
        }
      }
      return false;
    } catch (e) {
      Logger().e('UAE PASS callback processing error: $e');
      return false;
    }
  }

  static Future<String?> getRole() async {
    final token = await ApiService.getToken();
    if (token == null) return null;
    final payload = JwtUtils.decodeJwtPayload(token);
    if (payload == null) return null;
    // The claim name could be 'role', 'roles', or similar depending on your backend
    if (payload.containsKey('role')) {
      return payload['role'] as String?;
    } else if (payload.containsKey('roles')) {
      // If roles is a list, pick the first one
      final roles = payload['roles'];
      if (roles is List && roles.isNotEmpty) {
        return roles.first as String?;
      }
    }
    return null;
  }
}