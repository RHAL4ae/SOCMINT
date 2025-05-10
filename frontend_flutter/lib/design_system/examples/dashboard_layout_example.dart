import 'package:flutter/material.dart';
import '../index.dart';

/// SOCMINT Dashboard Layout Example
/// 
/// This file demonstrates how to implement the SOCMINT design system
/// in a complete dashboard layout. It shows proper usage of the sidebar,
/// top bar, and content area according to the design guidelines.

class DashboardLayoutExample extends StatelessWidget {
  const DashboardLayoutExample({super.key});

  @override
  Widget build(BuildContext context) {
    // No isRTL needed here as it is not used in this method.
    
    return Scaffold(
      body: Row(
        children: [
          // Left Sidebar (240px width)
          SidebarExample(),
          
          // Main Content Area
          Expanded(
            child: Column(
              children: [
                // Top Bar (64px height)
                TopBarExample(),
                
                // Main Content
                Expanded(
                  child: Container(
                    color: Theme.of(context).scaffoldBackgroundColor,
                    padding: const EdgeInsets.all(24),
                    child: DashboardContentExample(),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// Sidebar Example
class SidebarExample extends StatelessWidget {
  final int selectedIndex;

  const SidebarExample({super.key, this.selectedIndex = 0});

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;

    
    return Container(
      width: 240,
      color: SOCMINTColors.dark,
      child: Column(
        children: [
          // Logo area
          Container(
            height: 64,
            padding: const EdgeInsets.symmetric(horizontal: 16),
            alignment: Alignment.centerLeft,
            child: Row(
              children: [
                Container(
                  width: 32,
                  height: 32,
                  color: SOCMINTColors.primary,
                  child: Column(
                    children: [
                      Container(
                        height: 6,
                        color: SOCMINTColors.primary,
                      ),
                      const Spacer(),
                      const Text(
                        'رحّال',
                        style: TextStyle(
                          fontFamily: 'NotoKufiArabic',
                          fontSize: 14,
                          fontWeight: FontWeight.bold,
                          color: SOCMINTColors.primary,
                        ),
                        textAlign: TextAlign.center,
                        textDirection: TextDirection.rtl,
                      ),
                      const SizedBox(height: 4),
                    ],
                  ),
                ),
                const SizedBox(width: 12),
                Text(
                  'SOCMINT',
                  style: SOCMINTTextStyles.englishH3.copyWith(
                    color: SOCMINTColors.primary,
                  ),
                ),
              ],
            ),
          ),
          
          const SizedBox(height: 24),
          
          // Menu items
          _buildMenuItem(context, 0, Icons.dashboard, isRTL ? 'لوحة المعلومات' : 'Dashboard', selectedIndex == 0),
          _buildMenuItem(context, 1, Icons.search, isRTL ? 'البحث والتحليل' : 'Search & Analysis', selectedIndex == 1),
          _buildMenuItem(context, 2, Icons.people, isRTL ? 'الكيانات' : 'Entities', selectedIndex == 2),
          _buildMenuItem(context, 3, Icons.warning, isRTL ? 'التنبيهات' : 'Alerts', selectedIndex == 3),
          _buildMenuItem(context, 4, Icons.insert_chart, isRTL ? 'التقارير' : 'Reports', selectedIndex == 4),
          
          const Spacer(),
          
          // Bottom menu items
          _buildMenuItem(context, 5, Icons.settings, isRTL ? 'الإعدادات' : 'Settings', selectedIndex == 5),
          _buildMenuItem(context, 6, Icons.help, isRTL ? 'المساعدة' : 'Help', selectedIndex == 6),
          
          const SizedBox(height: 16),
        ],
      ),
    );
  }
  
  Widget _buildMenuItem(BuildContext context, int index, IconData icon, String label, bool isSelected) {

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
      decoration: BoxDecoration(
        color: isSelected ? SOCMINTColors.primary.withValues(alpha: 51) : SOCMINTColors.dark,
        borderRadius: BorderRadius.circular(8),
        border: isSelected 
            ? Border(
                left: BorderSide(
                  color: SOCMINTColors.secondary,
                  width: 4,
                ),
              )
            : null,
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: () {},
          borderRadius: BorderRadius.circular(8),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            child: Row(
              children: [
                Icon(
                  icon,
                  color: isSelected ? SOCMINTColors.primary : SOCMINTColors.secondary,
                  size: 20,
                ),
                const SizedBox(width: 16),
                Text(
                  label,
                  style: TextStyle(
                    fontFamily: Directionality.of(context) == TextDirection.rtl ? 'Dubai' : 'Montserrat',
                    fontSize: 14,
                    fontWeight: isSelected ? FontWeight.w600 : FontWeight.w400,
                    color: isSelected ? SOCMINTColors.primary : SOCMINTColors.secondary,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// Top Bar Example
class TopBarExample extends StatelessWidget {
  const TopBarExample({super.key});

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;

    
    return Container(
      height: 64,
      padding: const EdgeInsets.symmetric(horizontal: 24),
      decoration: BoxDecoration(
        color: Theme.of(context).appBarTheme.backgroundColor,
        boxShadow: [
          BoxShadow(
            color: SOCMINTColors.dark.withValues(alpha: 12),
            blurRadius: 4,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Row(
        children: [
          // Page title
          Text(
            isRTL ? 'لوحة المعلومات' : 'Dashboard',
            style: isRTL 
                ? SOCMINTTextStyles.arabicH3 
                : SOCMINTTextStyles.englishH3,
          ),
          
          const Spacer(),
          
          // Search
          Container(
            width: 240,
            height: 40,
            decoration: BoxDecoration(
              color: Theme.of(context).brightness == Brightness.light 
                  ? SOCMINTColors.primary.withValues(alpha: 51) 
                  : SOCMINTColors.dark.withValues(alpha: 76),
              borderRadius: BorderRadius.circular(8),
            ),
            padding: const EdgeInsets.symmetric(horizontal: 12),
            child: Row(
              children: [
                Icon(
                  Icons.search,
                  size: 20,
                  color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 127),
                ),
                const SizedBox(width: 8),
                Text(
                  isRTL ? 'بحث...' : 'Search...',
                  style: (isRTL ? SOCMINTTextStyles.arabicBody2 : SOCMINTTextStyles.englishBody2).copyWith(
                    color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 127),
                  ),
                ),
              ],
            ),
          ),
          
          const SizedBox(width: 16),
          
          // Notifications
          IconButton(
            icon: const Icon(Icons.notifications_outlined),
            onPressed: () {},
            tooltip: isRTL ? 'الإشعارات' : 'Notifications',
          ),
          
          // Language toggle
          IconButton(
            icon: const Icon(Icons.language),
            onPressed: () {},
            tooltip: isRTL ? 'تغيير اللغة' : 'Change Language',
          ),
          
          // User menu
          Row(
            children: [
              SOCMINTAvatar(
                initials: 'RA',
                size: 32,
              ),
              const SizedBox(width: 8),
              Text(
                'Rami Kamel',
                style: isRTL 
                    ? SOCMINTTextStyles.arabicBody1 
                    : SOCMINTTextStyles.englishBody1,
              ),
              IconButton(
                icon: const Icon(Icons.arrow_drop_down),
                onPressed: () {},
                splashRadius: 20,
              ),
            ],
          ),
        ],
      ),
    );
  }
}

/// Dashboard Content Example
class DashboardContentExample extends StatelessWidget {
  const DashboardContentExample({super.key});

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;

    
    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Alert section
          SOCMINTAlert(
            title: isRTL ? 'تنبيه أمني' : 'Security Alert',
            message: isRTL 
                ? 'تم اكتشاف 3 أنشطة مشبوهة في الساعات الـ 24 الماضية. يرجى مراجعة قسم التنبيهات.'
                : 'Detected 3 suspicious activities in the last 24 hours. Please review the Alerts section.',
            type: AlertType.warning,
            onClose: () {},
          ),
          
          const SizedBox(height: 24),
          
          // Stats cards
          GridView.count(
            crossAxisCount: 4,
            crossAxisSpacing: 24,
            mainAxisSpacing: 24,
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            children: [
              _buildStatCard(
                context,
                isRTL ? 'المصادر النشطة' : 'Active Sources',
                '24',
                Icons.cloud_done,
                SOCMINTColors.primary,
              ),
              _buildStatCard(
                context,
                isRTL ? 'الكيانات المكتشفة' : 'Entities Discovered',
                '1,284',
                Icons.people,
                SOCMINTColors.primary,
              ),
              _buildStatCard(
                context,
                isRTL ? 'التنبيهات الحرجة' : 'Critical Alerts',
                '7',
                Icons.warning,
                SOCMINTColors.accent,
              ),
              _buildStatCard(
                context,
                isRTL ? 'التقارير المولدة' : 'Reports Generated',
                '32',
                Icons.description,
                SOCMINTColors.dark,
              ),
            ],
          ),
          
          const SizedBox(height: 32),
          
          // Recent activities section
          SOCMINTSectionHeader(
            title: isRTL ? 'الأنشطة الأخيرة' : 'Recent Activities',
            action: SOCMINTTextButton(
              text: isRTL ? 'عرض الكل' : 'View All',
              onPressed: () {},
              icon: Icons.arrow_forward,
            ),
          ),
          
          SOCMINTCard(
            child: Column(
              children: [
                _buildActivityItem(
                  context,
                  isRTL ? 'تم اكتشاف حساب مشبوه' : 'Suspicious Account Detected',
                  isRTL ? 'تم تحديد حساب جديد مرتبط بنشاط مشبوه سابق' : 'New account identified linked to previous suspicious activity',
                  '2 hours ago',
                  Icons.security,
                  SOCMINTColors.accent,
                ),
                const SOCMINTDivider(),
                _buildActivityItem(
                  context,
                  isRTL ? 'تحليل الشبكة الاجتماعية مكتمل' : 'Social Network Analysis Complete',
                  isRTL ? 'تم الانتهاء من تحليل الشبكة لـ 156 كيان' : 'Network analysis completed for 156 entities',
                  '5 hours ago',
                  Icons.share,
                  SOCMINTColors.primary,
                ),
                const SOCMINTDivider(),
                _buildActivityItem(
                  context,
                  isRTL ? 'تقرير جديد جاهز' : 'New Report Ready',
                  isRTL ? 'تم إنشاء تقرير التحليل الأسبوعي وهو جاهز للمراجعة' : 'Weekly analysis report has been generated and is ready for review',
                  '1 day ago',
                  Icons.description,
                  SOCMINTColors.primary,
                ),
              ],
            ),
          ),
          
          const SizedBox(height: 32),
          
          // Two column layout
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Left column
              Expanded(
                flex: 2,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    SOCMINTSectionHeader(
                      title: isRTL ? 'الكيانات المكتشفة حديثًا' : 'Recently Discovered Entities',
                    ),
                    SOCMINTCard(
                      child: Column(
                        children: [
                          _buildEntityItem(
                            context,
                            'Ahmed Hassan',
                            isRTL ? 'شخص' : 'Person',
                            isRTL ? 'مرتبط بـ 5 حسابات' : 'Connected to 5 accounts',
                          ),
                          const SOCMINTDivider(),
                          _buildEntityItem(
                            context,
                            'Global Finance Ltd',
                            isRTL ? 'منظمة' : 'Organization',
                            isRTL ? 'مرتبط بـ 12 معاملة' : 'Connected to 12 transactions',
                          ),
                          const SOCMINTDivider(),
                          _buildEntityItem(
                            context,
                            '@tech_insider',
                            isRTL ? 'حساب' : 'Account',
                            isRTL ? 'نشاط مرتفع' : 'High activity',
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              
              const SizedBox(width: 24),
              
              // Right column
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    SOCMINTSectionHeader(
                      title: isRTL ? 'الإجراءات السريعة' : 'Quick Actions',
                    ),
                    SOCMINTCard(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          SOCMINTPrimaryButton(
                            text: isRTL ? 'إنشاء تقرير جديد' : 'Create New Report',
                            onPressed: () {},
                            icon: Icons.add,
                            isFullWidth: true,
                          ),
                          const SizedBox(height: 12),
                          SOCMINTSecondaryButton(
                            text: isRTL ? 'تحليل بيانات جديدة' : 'Analyze New Data',
                            onPressed: () {},
                            icon: Icons.analytics,
                            isFullWidth: true,
                          ),
                          const SizedBox(height: 12),
                          SOCMINTSecondaryButton(
                            text: isRTL ? 'إضافة مصدر بيانات' : 'Add Data Source',
                            onPressed: () {},
                            icon: Icons.add_circle,
                            isFullWidth: true,
                          ),
                        ],
                      ),
                    ),
                    
                    const SizedBox(height: 24),
                    
                    SOCMINTSectionHeader(
                      title: isRTL ? 'الوسوم الشائعة' : 'Popular Tags',
                    ),
                    SOCMINTCard(
                      child: Wrap(
                        spacing: 8,
                        runSpacing: 8,
                        children: [
                          SOCMINTBadge(text: 'Finance'),
                          SOCMINTBadge(text: 'Social Media'),
                          SOCMINTBadge(text: 'Dark Web'),
                          SOCMINTBadge(text: 'Crypto'),
                          SOCMINTBadge(text: 'UAE'),
                          SOCMINTBadge(text: 'Analysis'),
                          SOCMINTBadge(text: 'Entities'),
                          SOCMINTBadge(text: 'Reports'),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
  
  Widget _buildStatCard(BuildContext context, String title, String value, IconData icon, Color color) {
  final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    return SOCMINTCard(
      child: Column(
        crossAxisAlignment: isRTL ? CrossAxisAlignment.end : CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                  color: color.withValues(alpha: 26),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Icon(
                  icon,
                  color: color,
                  size: 24,
                ),
              ),
              const Spacer(),
              Icon(
                Icons.more_vert,
                color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 127),
                size: 20,
              ),
            ],
          ),
          const SizedBox(height: 16),
          Text(
            value,
            style: (isRTL ? SOCMINTTextStyles.arabicH2 : SOCMINTTextStyles.englishH2).copyWith(
              color: Theme.of(context).colorScheme.onSurface,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            title,
            style: (isRTL ? SOCMINTTextStyles.arabicBody2 : SOCMINTTextStyles.englishBody2).copyWith(
              color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 179),
            ),
          ),
        ],
      ),
    );
  }
  
  Widget _buildActivityItem(BuildContext context, String title, String description, String time, IconData icon, Color color) {
  final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              color: color.withValues(alpha: 26),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Icon(
              icon,
              color: color,
              size: 24,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: isRTL ? CrossAxisAlignment.end : CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: (isRTL ? SOCMINTTextStyles.arabicH4 : SOCMINTTextStyles.englishH4).copyWith(
                    color: Theme.of(context).colorScheme.onSurface,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  description,
                  style: (isRTL ? SOCMINTTextStyles.arabicBody2 : SOCMINTTextStyles.englishBody2).copyWith(
                    color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 178),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 16),
          Text(
            time,
            style: (isRTL ? SOCMINTTextStyles.arabicBody2 : SOCMINTTextStyles.englishBody2).copyWith(
              color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 127),
            ),
          ),
        ],
      ),
    );
  }
  
  Widget _buildEntityItem(BuildContext context, String name, String type, String info) {
  final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12),
      child: Row(
        children: [
          SOCMINTAvatar(
            initials: name.split(' ').map((e) => e[0]).take(2).join(''),
            size: 40,
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  name,
                  style: (isRTL ? SOCMINTTextStyles.arabicH4 : SOCMINTTextStyles.englishH4).copyWith(
                    color: Theme.of(context).colorScheme.onSurface,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  info,
                  style: (isRTL ? SOCMINTTextStyles.arabicBody2 : SOCMINTTextStyles.englishBody2).copyWith(
                    color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 178),
                  ),
                ),
              ],
            ),
          ),
          SOCMINTBadge(
            text: type,
            color: type == 'Person' || type == 'شخص' 
                ? SOCMINTColors.primary 
                : (type == 'Organization' || type == 'منظمة' 
                    ? SOCMINTColors.primary 
                    : SOCMINTColors.accent),
          ),
        ],
      ),
    );
  }
}