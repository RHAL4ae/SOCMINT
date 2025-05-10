import 'package:flutter/material.dart';
import '../widgets/navigation_drawer.dart';
import '../localization/intl_localizations.dart';

class DashboardAdminScreen extends StatelessWidget {
  const DashboardAdminScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final loc = SocmintLocalizations.of(context);
    return Scaffold(
      drawer: const NavigationDrawerWidget(),
      appBar: AppBar(
        title: Text(loc?.translate('dashboardAdmin') ?? 'Admin Dashboard'),
      ),
      body: Center(
        child: Text(
          loc?.translate('dashboardAdmin') ?? 'Admin Dashboard',
          style: Theme.of(context).textTheme.headlineMedium,
        ),
      ),
    );
  }
}