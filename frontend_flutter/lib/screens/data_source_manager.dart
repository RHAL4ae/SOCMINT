import 'package:flutter/material.dart';
import '../widgets/navigation_drawer.dart';
import '../localization/intl_localizations.dart';

class DataSourceManagerScreen extends StatelessWidget {
  const DataSourceManagerScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final loc = SocmintLocalizations.of(context);
    return Scaffold(
      drawer: const NavigationDrawerWidget(),
      appBar: AppBar(
        title: Text(loc?.translate('dataSourceManager') ?? 'Data Source Manager'),
      ),
      body: Center(
        child: Text(
          loc?.translate('dataSourceManager') ?? 'Data Source Manager',
          style: Theme.of(context).textTheme.headlineMedium,
        ),
      ),
    );
  }
}