import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import '../localization/intl_localizations.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  String _username = '';
  String _password = '';
  bool _loading = false;
  String? _error;

  Future<void> _login() async {
    setState(() {
      _loading = true;
      _error = null;
    });
    bool success = await AuthService.login(_username, _password);
    setState(() {
      _loading = false;
      if (!success) {
        _error = '${SocmintLocalizations.of(context)?.translate('login')} failed';
      }
    });
    if (success) {
      // TODO: Route based on role
      Navigator.pushReplacementNamed(context, '/dashboard/admin');
    }
  }

  @override
  Widget build(BuildContext context) {
    final loc = SocmintLocalizations.of(context);
    return Scaffold(
      body: Center(
        child: Card(
          elevation: 8,
          margin: const EdgeInsets.symmetric(horizontal: 24, vertical: 48),
          child: Padding(
            padding: const EdgeInsets.all(32.0),
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(loc?.translate('login') ?? 'Login', style: Theme.of(context).textTheme.headlineSmall),
                  const SizedBox(height: 24),
                  TextFormField(
                    decoration: InputDecoration(labelText: loc?.translate('username') ?? 'Username'),
                    onChanged: (v) => _username = v,
                    validator: (v) => v == null || v.isEmpty ? 'Required' : null,
                  ),
                  const SizedBox(height: 16),
                  TextFormField(
                    decoration: InputDecoration(labelText: loc?.translate('password') ?? 'Password'),
                    obscureText: true,
                    onChanged: (v) => _password = v,
                    validator: (v) => v == null || v.isEmpty ? 'Required' : null,
                  ),
                  const SizedBox(height: 24),
                  if (_error != null) ...[
                    Text(_error!, style: const TextStyle(color: Colors.red)),
                    const SizedBox(height: 12),
                  ],
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: _loading
                          ? null
                          : () {
                              if (_formKey.currentState?.validate() ?? false) {
                                _login();
                              }
                            },
                      child: _loading
                          ? const CircularProgressIndicator(strokeWidth: 2)
                          : Text(loc?.translate('login') ?? 'Login'),
                    ),
                  ),
                  const SizedBox(height: 16),
                  OutlinedButton(
                    onPressed: () async {
                      await AuthService.loginWithUAEPASS();
                    },
                    child: Text(loc?.translate('uaePass') ?? 'Login with UAE PASS'),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}