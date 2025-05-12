import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;

class UAEPassLoginButton extends StatelessWidget {
  const UAEPassLoginButton({super.key});

  Future<void> _handleLogin() async {
    try {
      // Get the login URL from the backend
      final response = await http.get(
        Uri.parse('https://socmint.ae/api/auth/uaepass/login'),
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = Map<String, dynamic>.from(
          json.decode(response.body),
        );
        
        final String authorizationUrl = data['authorization_url'];
        
        // Launch the UAE PASS login URL
        if (await canLaunchUrl(Uri.parse(authorizationUrl))) {
          await launchUrl(
            Uri.parse(authorizationUrl),
            mode: LaunchMode.externalApplication,
          );
        }
      }
    } catch (e) {
      print('Error during UAE PASS login: $e');
      // Show error to user
    }
  }

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _handleLogin,
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.blue,
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8),
        ),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Image.asset(
            'assets/images/uaepass_logo.png',
            width: 24,
            height: 24,
          ),
          const SizedBox(width: 8),
          const Text(
            'تسجيل الدخول عبر الهوية الرقمية',
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }
}
