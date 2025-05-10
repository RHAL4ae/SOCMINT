import 'package:flutter/material.dart';
import '../screens/login.dart';
import '../screens/dashboard_admin.dart';
import '../screens/dashboard_analyst.dart';
import '../screens/dashboard_viewer.dart';
import '../screens/data_source_manager.dart';
import '../screens/uaepass_callback.dart';

class AppRoutes {
  static const String login = '/login';
  static const String adminDashboard = '/dashboard/admin';
  static const String analystDashboard = '/dashboard/analyst';
  static const String viewerDashboard = '/dashboard/viewer';
  static const String dataSourceManager = '/data-source-manager';
  static const String uaePassCallback = '/auth/uaepass/callback';

  static final Map<String, WidgetBuilder> routes = {
    login: (context) => const LoginScreen(),
    adminDashboard: (context) => const DashboardAdminScreen(),
    analystDashboard: (context) => const DashboardAnalystScreen(),
    viewerDashboard: (context) => const DashboardViewerScreen(),
    dataSourceManager: (context) => const DataSourceManagerScreen(),
    uaePassCallback: (context) => const UAEPassCallbackScreen(),
  };
}