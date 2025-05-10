import 'package:flutter/material.dart';
import '../index.dart';

/// UAE PASS Login Button Example
/// 
/// This component demonstrates how to implement the UAE PASS login button
/// using the SOCMINT design system. It follows the visual identity guidelines
/// and supports both Arabic and English localization.

class UAEPassLoginButton extends StatelessWidget {
  final VoidCallback onPressed;
  final bool isLoading;
  
  const UAEPassLoginButton({
    super.key,
    required this.onPressed,
    this.isLoading = false,
  });
  
  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final String buttonText = isRTL 
        ? 'تسجيل الدخول عبر الهوية الرقمية'
        : 'Login with UAE PASS';
    
    return SOCMINTPrimaryButton(
      text: buttonText,
      onPressed: onPressed,
      isLoading: isLoading,
      icon: Icons.verified_user,
      isFullWidth: true,
    );
  }
}

/// UAE PASS Login Card Example
/// 
/// A complete login card that includes the UAE PASS login button
/// and demonstrates the design system in a real component.

class UAEPassLoginCard extends StatelessWidget {
  final VoidCallback onLoginPressed;
  final bool isLoading;
  
  const UAEPassLoginCard({
    super.key,
    required this.onLoginPressed,
    this.isLoading = false,
  });
  
  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final TextStyle headingStyle = isRTL 
        ? SOCMINTTextStyles.arabicH2 
        : SOCMINTTextStyles.englishH2;
    final TextStyle bodyStyle = isRTL 
        ? SOCMINTTextStyles.arabicBody1 
        : SOCMINTTextStyles.englishBody1;
    
    final String title = isRTL 
        ? 'مرحباً بك في منصة SOCMINT'
        : 'Welcome to SOCMINT Platform';
    
    final String description = isRTL 
        ? 'منصة الاستخبارات السيادية متعددة القنوات'
        : 'Sovereign Multi-Channel Intelligence Platform';
    
    return SOCMINTCard(
      width: 400,
      padding: const EdgeInsets.all(32),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          // Logo placeholder
          Container(
            width: 120,
            height: 60,
            color: SOCMINTColors.rhalDark,
            child: Column(
              children: [
                Container(
                  height: 8,
                  color: SOCMINTColors.rhalGreen,
                ),
                const SizedBox(height: 8),
                Text(
                  'رحّال',
                  style: const TextStyle(
                    fontFamily: 'Dubai',
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: SOCMINTColors.white,
                  ),
                  textDirection: TextDirection.rtl,
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),
          Text(
            title,
            style: headingStyle.copyWith(
              color: Theme.of(context).colorScheme.onSurface,
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),
          Text(
            description,
            style: bodyStyle.copyWith(
              color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.7),
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 32),
          UAEPassLoginButton(
            onPressed: onLoginPressed,
            isLoading: isLoading,
          ),
          const SizedBox(height: 16),
          Row(
            children: [
              const Expanded(child: SOCMINTDivider()),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: Text(
                  isRTL ? 'أو' : 'OR',
                  style: bodyStyle.copyWith(
                    color: SOCMINTColors.darkGray,
                  ),
                ),
              ),
              const Expanded(child: SOCMINTDivider()),
            ],
          ),
          const SizedBox(height: 16),
          SOCMINTSecondaryButton(
            text: isRTL ? 'تسجيل الدخول بالبريد الإلكتروني' : 'Login with Email',
            onPressed: onLoginPressed,
            icon: Icons.email,
            isFullWidth: true,
          ),
        ],
      ),
    );
  }
}