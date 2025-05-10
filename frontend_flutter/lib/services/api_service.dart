import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class ApiService {
  static final Dio _dio = Dio();
  static final FlutterSecureStorage _storage = const FlutterSecureStorage();
  
  // Base URL for the backend API
  static String get baseUrl => const String.fromEnvironment('API_BASE_URL', defaultValue: 'https://socmint.ae');

  static Future<void> setToken(String token) async {
    await _storage.write(key: 'jwt_token', value: token);
  }

  static Future<String?> getToken() async {
    return await _storage.read(key: 'jwt_token');
  }

  static Future<void> clearToken() async {
    await _storage.delete(key: 'jwt_token');
  }

  static Future<Response> request(String path, {String method = 'GET', Map<String, dynamic>? data, Map<String, dynamic>? queryParameters}) async {
    final token = await getToken();
    final options = Options(
      method: method,
      headers: token != null ? {'Authorization': 'Bearer $token'} : {},
    );
    try {
      return await _dio.request(
        path,
        data: data,
        queryParameters: queryParameters,
        options: options,
      );
    } on DioException {
      // Handle error globally
      rethrow;
    }
  }
}