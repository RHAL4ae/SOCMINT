import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import '../localization/intl_localizations.dart';
import '../widgets/uaepass_login_button.dart';

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
      // Route based on role
      final role = await AuthService.getRole();
      if (!mounted) return;
      if (role == 'admin') {
        Navigator.pushReplacementNamed(context, '/dashboard/admin');
      } else if (role == 'analyst') {
        Navigator.pushReplacementNamed(context, '/dashboard/analyst');
      } else if (role == 'viewer') {
        Navigator.pushReplacementNamed(context, '/dashboard/viewer');
      } else {
        // Default fallback
        Navigator.pushReplacementNamed(context, '/dashboard/admin');
      }
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
                    decoration: InputDecoration(
                      labelText: loc?.translate('username') ?? 'Username',
                    ),
                    onChanged: (val) => _username = val,
                    validator: (val) => val == null || val.isEmpty ? '${loc?.translate('username') ?? 'Username'} ${loc?.translate('required') ?? 'is required'}' : null,
                  ),
                  const SizedBox(height: 16),
                  TextFormField(
                    decoration: InputDecoration(labelText: loc?.translate('password') ?? 'Password'),
                    obscureText: true,
                    onChanged: (val) => _password = val,
                    validator: (val) => val == null || val.isEmpty ? '${loc?.translate('password') ?? 'Password'} ${loc?.translate('required') ?? 'is required'}' : null,
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
                  const UAEPassLoginButton(),
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