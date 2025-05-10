import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:provider/provider.dart';
import '../../services/auth_service.dart';
import '../../assets/theme/theme_data.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Logo
            Padding(
              padding: const EdgeInsets.all(32.0),
              child: Image.asset(
                'assets/images/logo/logo_primary.png',
                width: 128,
              ),
            ),
            // Welcome text
            Text(
              AppLocalizations.of(context)!.welcome,
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            const SizedBox(height: 16),
            Text(
              AppLocalizations.of(context)!.loginToContinue,
              style: Theme.of(context).textTheme.bodyLarge,
            ),
            const SizedBox(height: 32),
            // UAE PASS login button
            Consumer<AuthService>(
              builder: (context, authService, child) {
                if (authService.isLoading) {
                  return const CircularProgressIndicator();
                }
                return ElevatedButton.icon(
                  onPressed: () => authService.loginWithUaePass(),
                  icon: Image.asset(
                    'assets/images/uaepass_logo.png',
                    width: 24,
                  ),
                  label: Text(
                    AppLocalizations.of(context)!.loginWithUaePass,
                    style: const TextStyle(fontSize: 16),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppTheme.primaryGreen,
                    padding: const EdgeInsets.symmetric(
                      horizontal: 32,
                      vertical: 16,
                    ),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(8),
                    ),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
