import 'package:flutter/material.dart';
import '../services/auth_service.dart';

class UAEPassCallbackScreen extends StatefulWidget {
  const UAEPassCallbackScreen({Key? key}) : super(key: key);

  @override
  State<UAEPassCallbackScreen> createState() => _UAEPassCallbackScreenState();
}

class _UAEPassCallbackScreenState extends State<UAEPassCallbackScreen> {
  bool _loading = true;
  String? _error;

  @override
  void initState() {
    super.initState();
    _processCallback();
  }

  Future<void> _processCallback() async {
    try {
      final currentUrl = Uri.base.toString();
      final success = await AuthService.processUAEPassCallback(currentUrl);
      
      if (success) {
        // Navigate to appropriate dashboard based on role
        // For now, default to admin dashboard
        if (mounted) {
          Navigator.pushReplacementNamed(context, '/dashboard/admin');
        }
      } else {
        setState(() {
          _loading = false;
          _error = 'Failed to process UAE PASS authentication';
        });
      }
    } catch (e) {
      setState(() {
        _loading = false;
        _error = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: _loading
            ? const Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  CircularProgressIndicator(),
                  SizedBox(height: 16),
                  Text('Processing UAE PASS authentication...'),
                ],
              )
            : Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.error_outline, color: Colors.red, size: 48),
                  const SizedBox(height: 16),
                  Text(_error ?? 'Authentication failed'),
                  const SizedBox(height: 24),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.pushReplacementNamed(context, '/login');
                    },
                    child: const Text('Return to Login'),
                  ),
                ],
              ),
      ),
    );
  }
}