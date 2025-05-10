import 'dart:convert';

class JwtUtils {
  static Map<String, dynamic>? decodeJwtPayload(String token) {
    try {
      final parts = token.split('.');
      if (parts.length != 3) {
        return null;
      }
      final payload = parts[1];
      var normalized = base64Url.normalize(payload);
      final payloadMap = json.decode(utf8.decode(base64Url.decode(normalized)));
      if (payloadMap is! Map<String, dynamic>) {
        return null;
      }
      return payloadMap;
    } catch (e) {
      return null;
    }
  }
}
