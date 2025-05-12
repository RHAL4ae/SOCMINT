import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../assets/theme/theme_data.dart';
import '../../assets/theme/components/dashboard_components.dart';
import 'package:sizer/sizer.dart';
import 'package:flutter_svg/flutter_svg.dart';
import '../../assets/theme/components/chart_components.dart';
import '../../services/navigation_service.dart';
import '../../services/auth_service.dart';
import '../../services/theme_service.dart';
import '../../services/language_service.dart';
import '../../assets/images/logo/logo_variants.dart';
import '../../widgets/profile/uaepass_profile_widget.dart';

// Add missing components
class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  int _selectedIndex = 0;
  bool _isDarkMode = false;
  final TextEditingController _searchController = TextEditingController();



  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Logo.primary(width: 32),
            const SizedBox(width: 8),
            Text(
              'Dashboard',
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
                  Logo.primary(width: 48),
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
            const UAEPassProfileWidget(),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.dashboard),
              title: Text('Dashboard'),
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
              title: Text('Analytics'),
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
              title: Text('Reports'),
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
              title: Text('Settings'),
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
                    child: TextField(
                      controller: _searchController,
                      decoration: InputDecoration(
                        hintText: 'Search...',
                        prefixIcon: const Icon(Icons.search),
                        suffixIcon: IconButton(
                          icon: const Icon(Icons.filter_list),
                          onPressed: () {
                            // Implement filter functionality
                          },
                        ),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(8),
                        ),
                      ),
                      onChanged: (value) {
                        // Implement search functionality
                      },
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              Text(
                'Dashboard',
                style: Theme.of(context).textTheme.headlineMedium,
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Key Performance Indicators',
                          style: Theme.of(context).textTheme.headlineSmall,
                        ),
                        const SizedBox(height: 16),
                        Row(
                          children: [
                            Expanded(
                              child: KPIWidget(
                                title: 'Total Users',
                                value: '1,234',
                                color: AppTheme.primaryGreen,
                                icon: Icons.group,
                              ),
                            ),
                            const SizedBox(width: 16),
                            Expanded(
                              child: KPIWidget(
                                title: 'Active Users',
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
                                title: 'Total Posts',
                                value: '4,567',
                                color: AppTheme.primaryGreen,
                                icon: Icons.article,
                              ),
                            ),
                            const SizedBox(width: 16),
                            Expanded(
                              child: KPIWidget(
                                title: 'Engagement Rate',
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
                          'Recent Activity',
                          style: Theme.of(context).textTheme.headlineSmall,
                        ),
                        const SizedBox(height: 16),
                        Expanded(
                          child: ListView.builder(
                            itemCount: 5,
                            itemBuilder: (context, index) {
                              return AlertWidget(
                                title: 'New Post',
                                message: 'User posted an update',
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
                'Analytics',
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
