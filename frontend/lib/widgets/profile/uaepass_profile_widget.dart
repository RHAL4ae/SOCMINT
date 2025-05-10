import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import '../../services/auth_service.dart';
import '../../models/user.dart';

class UAEPassProfileWidget extends StatelessWidget {
  const UAEPassProfileWidget({super.key});

  @override
  Widget build(BuildContext context) {
    final authService = Provider.of<AuthService>(context);
    final loc = AppLocalizations.of(context)!;

    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  loc!.profileTitle,
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                IconButton(
                  icon: const Icon(Icons.edit),
                  onPressed: () {
                    // Implement profile edit functionality
                  },
                ),
              ],
            ),
            const SizedBox(height: 16),
            _buildProfileField(
              context,
              label: loc.logoutionalId,
              value: authService.nationalId ?? '',
            ),
            const SizedBox(height: 8),
            _buildProfileField(
              context,
              label: loc.userName,
              value: authService.userName ?? '',
            ),
            const SizedBox(height: 8),
            _buildLogoutButton(context),
          ],
        ),
      ),
    );
  }

  Widget _buildProfileField(BuildContext context, {
    required String label,
    required String value,
  }) {
    return Row(
      children: [
        Expanded(
          flex: 2,
          child: Text(
            label,
            style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
          ),
        ),
        Expanded(
          flex: 3,
          child: Text(
            value,
            style: Theme.of(context).textTheme.bodyLarge,
          ),
        ),
      ],
    );
  }

  Widget _buildLogoutButton(BuildContext context) {
    return ElevatedButton.icon(
      onPressed: () async {
        final authService = Provider.of<AuthService>(context, listen: false);
        await authService.logout();
        if (context.mounted) {
          Navigator.pushReplacementNamed(context, '/login');
        }
      },
      icon: const Icon(Icons.logout),
      label: Text(loc.logout),
    );
  }
}
