import 'package:flutter/material.dart';
import '../widgets/navigation_drawer.dart';
import '../localization/intl_localizations.dart';

class DashboardViewerScreen extends StatelessWidget {
  const DashboardViewerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final loc = SocmintLocalizations.of(context);
    return Scaffold(
      drawer: const NavigationDrawerWidget(),
      appBar: AppBar(
        title: Text(loc?.translate('dashboardViewer') ?? 'Viewer Dashboard'),
      ),
      body: Center(
        child: Text(
          loc?.translate('dashboardViewer') ?? 'Viewer Dashboard',
          style: Theme.of(context).textTheme.headlineMedium,
        ),
      ),
    );
  }
}