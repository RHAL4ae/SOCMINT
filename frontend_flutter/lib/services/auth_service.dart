import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'api_service.dart';
import 'dart:js' as js;

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
      if (Uri.base.toString().contains('localhost') || Uri.base.toString().contains('socmint.ae')) {
        // Web implementation
        final jsCode = "window.location.href = '$uaePassLoginUrl'";
        js.context.callMethod('eval', [jsCode]);
        return true; // This won't actually return as page will redirect
      } else {
        // TODO: Implement mobile version with url_launcher or webview
        throw Exception('Mobile implementation not available yet');
      }
    } catch (e) {
      print('UAE PASS login error: $e');
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
      print('UAE PASS callback processing error: $e');
      return false;
    }
  }

  static Future<String?> getRole() async {
    // TODO: Implement role extraction from JWT or backend
    return null;
  }
}