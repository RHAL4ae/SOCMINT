import 'package:http/http.dart' as http;
import 'package:flutter/foundation.dart';
import 'package:jwt_decoder/jwt_decoder.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'dart:convert';
import '../models/user.dart';

class AuthService with ChangeNotifier {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();
  String? _accessToken;
  String? _idToken;
  String? _refreshToken;
  String? _userName;
  String? _nationalId;
  bool _isLoading = false;
  User? _currentUser;

  User? get currentUser => _currentUser;

  AuthService() {
    _loadTokens();
  }

  bool get isLoading => _isLoading;
  String? get userName => _userName;
  String? get nationalId => _nationalId;

  Future<void> initAuth() async {
    await _loadTokens();
  }

  Future<void> _loadTokens() async {
    _accessToken = await _storage.read(key: 'access_token');
    _idToken = await _storage.read(key: 'id_token');
    _refreshToken = await _storage.read(key: 'refresh_token');
    _userName = await _storage.read(key: 'user_name');
    _nationalId = await _storage.read(key: 'national_id');
    notifyListeners();
  }

  Future<void> loginWithUaePass() async {
    try {
      _isLoading = true;
      notifyListeners();

      // Get configuration from .env
      final clientId = const String.fromEnvironment('UAE_PASS_CLIENT_ID');
      final clientSecret = const String.fromEnvironment('UAE_PASS_CLIENT_SECRET');
      final authUrl = const String.fromEnvironment('UAE_PASS_AUTH_URL');
      final tokenUrl = const String.fromEnvironment('UAE_PASS_TOKEN_URL');
      final userInfoUrl = const String.fromEnvironment('UAE_PASS_USERINFO_URL');
      final redirectUri = const String.fromEnvironment('REDIRECT_URI');

      // Generate nonce
      final nonce = DateTime.now().millisecondsSinceEpoch.toString();

      // Redirect to UAE PASS
      Uri.parse(authUrl).replace(
        queryParameters: {
          'client_id': clientId,
          'response_type': 'code',
          'redirect_uri': redirectUri,
          'scope': 'openid profile',
          'nonce': nonce,
        },
      );

      // Handle callback
      final code = await _handleCallback();

      // Exchange code for tokens
      final tokenResponse = await http.post(
        Uri.parse(tokenUrl),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: {
          'grant_type': 'authorization_code',
          'client_id': clientId,
          'client_secret': clientSecret,
          'code': code,
          'redirect_uri': redirectUri,
        },
      );

      if (tokenResponse.statusCode == 200) {
        final tokenData = json.decode(tokenResponse.body);
        _accessToken = tokenData['access_token'];
        _idToken = tokenData['id_token'];
        _refreshToken = tokenData['refresh_token'];

        // Validate tokens
        if (_validateTokens()) {
          // Get user info
          final userInfoResponse = await http.get(
            Uri.parse(userInfoUrl),
            headers: {
              'Authorization': 'Bearer $_accessToken',
            },
          );

          if (userInfoResponse.statusCode == 200) {
            final userInfo = json.decode(userInfoResponse.body);
            _userName = userInfo['name'];
            _nationalId = userInfo['national_id'];

            // Save tokens and user info
            _saveTokens();
            notifyListeners();
          }
        }
      }
    } catch (e) {
      debugPrint('Login error: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<String> _handleCallback() async {
    // Implement callback handling logic
    // This will depend on your platform (web or mobile)
    throw UnimplementedError('Callback handling not implemented');
  }

  bool _validateTokens() {
    try {
      if (_idToken == null || _accessToken == null) return false;

      // Validate ID token
      final idTokenClaims = JwtDecoder.decode(_idToken!);

      // Check expiration
      if (JwtDecoder.isExpired(_idToken!) || JwtDecoder.isExpired(_accessToken!)) {
        return false;
      }

      // Check audience
      if (idTokenClaims['aud'] != const String.fromEnvironment('UAE_PASS_CLIENT_ID')) {
        return false;
      }

      // Check nonce (implement nonce verification)
      // Check issuer
      // Check signature

      return true;
    } catch (e) {
      debugPrint('Token validation error: $e');
      return false;
    }
  }

  void _saveTokens() {
    _storage.write(key: 'access_token', value: _accessToken!);
    _storage.write(key: 'id_token', value: _idToken!);
    _storage.write(key: 'refresh_token', value: _refreshToken!);
    _storage.write(key: 'user_name', value: _userName!);
    _storage.write(key: 'national_id', value: _nationalId!);
  }

  Future<void> logout() async {
    _accessToken = null;
    _idToken = null;
    _refreshToken = null;
    _userName = null;
    _nationalId = null;
    _currentUser = null;

    await _storage.deleteAll();
    notifyListeners();
  }

  bool get isAuthenticated {
    return _accessToken != null && _idToken != null;
  }
}
