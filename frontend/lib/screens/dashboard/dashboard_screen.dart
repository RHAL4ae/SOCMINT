import 'package:flutter/material.dart' as material;
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import '../../assets/theme/theme_data.dart';
import '../../assets/theme/components/dashboard_components.dart';
import 'package:sizer/sizer.dart';
import 'package:flutter_svg/flutter_svg.dart';
import '../../assets/theme/components/chart_components.dart';
import '../../services/navigation_service.dart';
import '../../services/auth_service.dart';
import '../../services/theme_service.dart';
import 'package:flutter/material.dart';
import '../../services/language_service.dart';
import '../../assets/images/logo/logo_variants.dart';
import '../../widgets/profile/uaepass_profile_widget.dart';

// Add missing components
Widget _HomeView() => const Center(child: Text('Home View'));
Widget _AnalyticsView() => const Center(child: Text('Analytics View'));
Widget _ReportsView() => const Center(child: Text('Reports View'));
Widget _SettingsView() => const Center(child: Text('Settings View'));



class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  int _selectedIndex = 0;
  bool _isDarkMode = false;
  final TextEditingController _searchController = TextEditingController();

  static List<Widget> _widgetOptions = [
    _HomeView(),
    _AnalyticsView(),
    _ReportsView(),
    _SettingsView(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Logo.getPrimary(width: 32),
            const SizedBox(width: 8),
            Text(
              AppLocalizations.of(context)!.dashboardTitle,
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: Icon(
              _isDarkMode ? Icons.light_mode : Icons.dark_mode,
              color: Colors.white,
            ),
            onPressed: () {
              setState(() {
                _isDarkMode = !_isDarkMode;
                // Implement theme toggle logic here
              });
            },
          ),
          IconButton(
            icon: const Icon(Icons.language),
            onPressed: () {
              // Implement language switch logic here
            },
          ),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                color: AppTheme.primaryGreen,
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Logo.getPrimary(width: 48),
                  const SizedBox(height: 8),
                  Text(
                    'RHAL',
                    style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                          color: Colors.white,
                        ),
                  ),
                  Text(
                    'عجمان للتقنيات المتقدمة',
                    style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                          color: Colors.white,
                        ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const UAEPassProfileWidget(),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.dashboard),
              title: Text(AppLocalizations.of(context)!.dashboardTitle),
              selected: _selectedIndex == 0,
              onTap: () {
                setState(() {
                  _selectedIndex = 0;
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: const Icon(Icons.analytics),
              title: Text(AppLocalizations.of(context)!.analyticsTitle),
              selected: _selectedIndex == 1,
              onTap: () {
                setState(() {
                  _selectedIndex = 1;
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: const Icon(Icons.report),
              title: Text(AppLocalizations.of(context)!.reportsTitle),
              selected: _selectedIndex == 2,
              onTap: () {
                setState(() {
                  _selectedIndex = 2;
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: const Icon(Icons.settings),
              title: Text(AppLocalizations.of(context)!.settingsTitle),
              selected: _selectedIndex == 3,
              onTap: () {
                setState(() {
                  _selectedIndex = 3;
                });
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: material.SearchBar(
                      controller: TextEditingController(),
                      onChanged: (value) {
                        // Implement search functionality
                      },
                      onSubmitted: (value) {
                        // Clear search functionality
                      },
                    ),
                  ),
                  const SizedBox(width: 16),
                  ElevatedButton.icon(
                    onPressed: () {
                      // Implement filter functionality
                    },
                    icon: const Icon(Icons.filter_list),
                    label: Text(AppLocalizations.of(context)!.filters),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              Row(
                children: [
                  Expanded(
                    flex: 2,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          AppLocalizations.of(context)!.keyPerformanceIndicators,
                          style: Theme.of(context).textTheme.headlineSmall,
                        ),
                        const SizedBox(height: 16),
                        Row(
                          children: [
                            Expanded(
                              child: KPIWidget(
                                title: AppLocalizations.of(context)!.totalUsers,
                                value: '1,234',
                                color: AppTheme.primaryGreen,
                                icon: Icons.group,
                              ),
                            ),
                            const SizedBox(width: 16),
                            Expanded(
                              child: KPIWidget(
                                title: AppLocalizations.of(context)!.activeUsers,
                                value: '856',
                                color: AppTheme.primaryGreen,
                                icon: Icons.people,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 16),
                        Row(
                          children: [
                            Expanded(
                              child: KPIWidget(
                                title: AppLocalizations.of(context)!.totalPosts,
                                value: '4,567',
                                color: AppTheme.primaryGreen,
                                icon: Icons.article,
                              ),
                            ),
                            const SizedBox(width: 16),
                            Expanded(
                              child: KPIWidget(
                                title: AppLocalizations.of(context)!.engagementRate,
                                value: '87%',
                                color: AppTheme.primaryGreen,
                                icon: Icons.trending_up,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 24),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          AppLocalizations.of(context)!.recentActivity,
                          style: Theme.of(context).textTheme.headlineSmall,
                        ),
                        const SizedBox(height: 16),
                        Expanded(
                          child: ListView.builder(
                            itemCount: 5,
                            itemBuilder: (context, index) {
                              return AlertWidget(
                                title: AppLocalizations.of(context)!.newPost,
                                message: AppLocalizations.of(context)!.userPostedUpdate,
                                color: AppTheme.primaryGreen,
                                icon: Icons.notifications,
                                onTap: () {
                                  // Navigate to post details
                                },
                              );
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              Text(
                AppLocalizations.of(context)!.analytics,
                style: Theme.of(context).textTheme.headlineSmall,
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          AppLocalizations.of(context)!.userEngagement,
                          style: Theme.of(context).textTheme.headlineMedium,
                        ),
                        const SizedBox(height: 16),
                        Expanded(
                          child: LineChartWidget(
                            data: [
                              {'label': 'Jan', 'value': 100},
                              {'label': 'Feb', 'value': 150},
                              {'label': 'Mar', 'value': 200},
                              {'label': 'Apr', 'value': 250},
                              {'label': 'May', 'value': 300},
                            ],
                            title: AppLocalizations.of(context)!.monthlyEngagement,
                            subtitle: AppLocalizations.of(context)!.userInteractionOverTime,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 24),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          AppLocalizations.of(context)!.userDemographics,
                          style: Theme.of(context).textTheme.headlineMedium,
                        ),
                        const SizedBox(height: 16),
                        Expanded(
                          child: PieChartWidget(
                            data: [
                              {'label': 'Male', 'value': 55, 'color': AppTheme.primaryGreen},
                              {'label': 'Female', 'value': 45, 'color': AppTheme.accentRed},
                            ],
                            title: AppLocalizations.of(context)!.genderDistribution,
                            subtitle: AppLocalizations.of(context)!.userDemographicsBreakdown,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
    );
  }
}

enum SettingType {
  darkMode,
  language,
  theme,
}

class _SettingItem extends StatelessWidget {
  final SettingType type;

  const _SettingItem({
    required this.type,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8.0),
      child: Row(
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  _getTitle(context),
                  style: Theme.of(context).textTheme.bodyLarge,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  String _getTitle(BuildContext context) {
    switch (type) {
      case SettingType.darkMode:
        return AppLocalizations.of(context)!.darkMode;
      case SettingType.language:
        return AppLocalizations.of(context)!.language;
      case SettingType.theme:
        return AppLocalizations.of(context)!.theme;
    }
  }
}
