import 'package:flutter/material.dart';
import '../widgets/navigation_drawer.dart';
import '../localization/intl_localizations.dart';

class DashboardAnalystScreen extends StatelessWidget {
  const DashboardAnalystScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final loc = SocmintLocalizations.of(context);
    return Scaffold(
      drawer: const NavigationDrawerWidget(),
      appBar: AppBar(
        title: Text(loc?.translate('dashboardAnalyst') ?? 'Analyst Dashboard'),
      ),
      body: Center(
        child: Text(
          loc?.translate('dashboardAnalyst') ?? 'Analyst Dashboard',
          style: Theme.of(context).textTheme.headlineMedium,
        ),
      ),
    );
  }
}