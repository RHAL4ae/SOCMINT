import 'package:flutter/material.dart';
import '../localization/intl_localizations.dart';

class NavigationDrawerWidget extends StatelessWidget {
  const NavigationDrawerWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final loc = SocmintLocalizations.of(context);
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          DrawerHeader(
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor,
            ),
            child: Center(
              child: Text(
                loc?.translate('appTitle') ?? 'SOCMINT Dashboard',
                style: const TextStyle(color: Colors.white, fontSize: 22, fontWeight: FontWeight.bold),
              ),
            ),
          ),
          ListTile(
            leading: const Icon(Icons.dashboard),
            title: Text(loc?.translate('dashboardAdmin') ?? 'Admin Dashboard'),
            onTap: () => Navigator.pushReplacementNamed(context, '/dashboard/admin'),
          ),
          ListTile(
            leading: const Icon(Icons.analytics),
            title: Text(loc?.translate('dashboardAnalyst') ?? 'Analyst Dashboard'),
            onTap: () => Navigator.pushReplacementNamed(context, '/dashboard/analyst'),
          ),
          ListTile(
            leading: const Icon(Icons.visibility),
            title: Text(loc?.translate('dashboardViewer') ?? 'Viewer Dashboard'),
            onTap: () => Navigator.pushReplacementNamed(context, '/dashboard/viewer'),
          ),
          ListTile(
            leading: const Icon(Icons.storage),
            title: Text(loc?.translate('dataSourceManager') ?? 'Data Source Manager'),
            onTap: () => Navigator.pushReplacementNamed(context, '/data-source-manager'),
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.logout),
            title: Text(loc?.translate('logout') ?? 'Logout'),
            onTap: () {
              Navigator.pushReplacementNamed(context, '/login');
            },
          ),
        ],
      ),
    );
  }
}