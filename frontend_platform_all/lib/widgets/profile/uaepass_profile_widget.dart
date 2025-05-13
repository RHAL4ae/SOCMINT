import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../localization/intl_localizations.dart';
import '../../services/auth_service.dart';
import '../../models/user.dart';

class UAEPassProfileWidget extends StatefulWidget { // Changed to StatefulWidget
  const UAEPassProfileWidget({super.key});

  @override
  State<UAEPassProfileWidget> createState() => _UAEPassProfileWidgetState();
}

class _UAEPassProfileWidgetState extends State<UAEPassProfileWidget> { // New State class
  String? _nationalId;
  String? _userName;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _fetchUserData();
  }

  Future<void> _fetchUserData() async {
    final nationalId = await AuthService.getNationalIdFromToken();
    final userName = await AuthService.getUserNameFromToken();
    if (mounted) {
      setState(() {
        _nationalId = nationalId;
        _userName = userName;
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    // final authService = Provider.of<AuthService>(context); // No longer needed directly for user data
    final loc = SocmintLocalizations.of(context);

    if (_isLoading) {
      return const Center(child: CircularProgressIndicator());
    }

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
                  loc.profileTitle, // Removed '!' as loc is already non-null
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
              label: loc.nationalId,
              value: _nationalId ?? '', // Use state variable
            ),
            const SizedBox(height: 8),
            _buildProfileField(
              context,
              label: loc.userName,
              value: _userName ?? '', // Use state variable
            ),
            const SizedBox(height: 8),
            _buildLogoutButton(context, loc), // Pass loc to the method
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

  Widget _buildLogoutButton(BuildContext context, AppLocalizations loc) {
    return ElevatedButton.icon(
      onPressed: () async {
        await AuthService.logout();
        if (context.mounted) {
          Navigator.pushReplacementNamed(context, '/login');
        }
      },
      icon: const Icon(Icons.logout),
      label: Text(loc.logout),
    );
  }
}
