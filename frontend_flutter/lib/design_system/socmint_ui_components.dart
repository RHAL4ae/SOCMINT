import 'package:flutter/material.dart';
import 'socmint_theme.dart';

/// SOCMINT UI Components
/// 
/// This file implements reusable UI components based on the SOCMINT design system.
/// These components maintain consistent styling across the application.

/// Primary button with RHAL green background
class SOCMINTPrimaryButton extends StatelessWidget {
  final String text;
  final VoidCallback onPressed;
  final bool isLoading;
  final bool isFullWidth;
  final IconData? icon;

  const SOCMINTPrimaryButton({
    Key? key,
    required this.text,
    required this.onPressed,
    this.isLoading = false,
    this.isFullWidth = false,
    this.icon,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final TextStyle textStyle = isRTL 
        ? SOCMINTTextStyles.arabicButton 
        : SOCMINTTextStyles.englishButton;
    
    return SizedBox(
      width: isFullWidth ? double.infinity : null,
      child: ElevatedButton(
        onPressed: isLoading ? null : onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: SOCMINTColors.rhalGreen,
          foregroundColor: SOCMINTColors.white,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          elevation: 2,
        ),
        child: isLoading
            ? const SizedBox(
                width: 20,
                height: 20,
                child: CircularProgressIndicator(
                  strokeWidth: 2,
                  valueColor: AlwaysStoppedAnimation<Color>(SOCMINTColors.white),
                ),
              )
            : Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  if (icon != null && !isRTL) Icon(icon, size: 18, color: SOCMINTColors.white),
                  if (icon != null && !isRTL) const SizedBox(width: 8),
                  Text(text, style: textStyle),
                  if (icon != null && isRTL) const SizedBox(width: 8),
                  if (icon != null && isRTL) Icon(icon, size: 18, color: SOCMINTColors.white),
                ],
              ),
      ),
    );
  }
}

/// Secondary button with outline
class SOCMINTSecondaryButton extends StatelessWidget {
  final String text;
  final VoidCallback onPressed;
  final bool isLoading;
  final bool isFullWidth;
  final IconData? icon;

  const SOCMINTSecondaryButton({
    Key? key,
    required this.text,
    required this.onPressed,
    this.isLoading = false,
    this.isFullWidth = false,
    this.icon,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final TextStyle textStyle = isRTL 
        ? SOCMINTTextStyles.arabicButton 
        : SOCMINTTextStyles.englishButton;
    
    return SizedBox(
      width: isFullWidth ? double.infinity : null,
      child: OutlinedButton(
        onPressed: isLoading ? null : onPressed,
        style: OutlinedButton.styleFrom(
          foregroundColor: SOCMINTColors.rhalGreen,
          side: const BorderSide(color: SOCMINTColors.rhalGreen),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
        child: isLoading
            ? const SizedBox(
                width: 20,
                height: 20,
                child: CircularProgressIndicator(
                  strokeWidth: 2,
                  valueColor: AlwaysStoppedAnimation<Color>(SOCMINTColors.rhalGreen),
                ),
              )
            : Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  if (icon != null && !isRTL) Icon(icon, size: 18),
                  if (icon != null && !isRTL) const SizedBox(width: 8),
                  Text(text, style: textStyle),
                  if (icon != null && isRTL) const SizedBox(width: 8),
                  if (icon != null && isRTL) Icon(icon, size: 18),
                ],
              ),
      ),
    );
  }
}

/// Text button (tertiary)
class SOCMINTTextButton extends StatelessWidget {
  final String text;
  final VoidCallback onPressed;
  final IconData? icon;

  const SOCMINTTextButton({
    Key? key,
    required this.text,
    required this.onPressed,
    this.icon,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final TextStyle textStyle = isRTL 
        ? SOCMINTTextStyles.arabicButton 
        : SOCMINTTextStyles.englishButton;
    
    return TextButton(
      onPressed: onPressed,
      style: TextButton.styleFrom(
        foregroundColor: SOCMINTColors.rhalGreen,
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (icon != null && !isRTL) Icon(icon, size: 18),
          if (icon != null && !isRTL) const SizedBox(width: 8),
          Text(text, style: textStyle),
          if (icon != null && isRTL) const SizedBox(width: 8),
          if (icon != null && isRTL) Icon(icon, size: 18),
        ],
      ),
    );
  }
}

/// Card with SOCMINT styling
class SOCMINTCard extends StatelessWidget {
  final Widget child;
  final EdgeInsetsGeometry? padding;
  final double? width;
  final double? height;
  final VoidCallback? onTap;

  const SOCMINTCard({
    Key? key,
    required this.child,
    this.padding,
    this.width,
    this.height,
    this.onTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(12),
      child: Container(
        width: width,
        height: height,
        decoration: BoxDecoration(
          color: Theme.of(context).cardTheme.color,
          borderRadius: BorderRadius.circular(12),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.1),
              blurRadius: 8,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        padding: padding ?? const EdgeInsets.all(16),
        child: child,
      ),
    );
  }
}

/// Text input with SOCMINT styling
class SOCMINTTextField extends StatelessWidget {
  final String? label;
  final String? hint;
  final TextEditingController? controller;
  final bool obscureText;
  final TextInputType keyboardType;
  final String? Function(String?)? validator;
  final void Function(String)? onChanged;
  final IconData? prefixIcon;
  final Widget? suffix;
  final bool isRequired;
  final bool enabled;
  final int? maxLines;
  final int? minLines;

  const SOCMINTTextField({
    Key? key,
    this.label,
    this.hint,
    this.controller,
    this.obscureText = false,
    this.keyboardType = TextInputType.text,
    this.validator,
    this.onChanged,
    this.prefixIcon,
    this.suffix,
    this.isRequired = false,
    this.enabled = true,
    this.maxLines = 1,
    this.minLines,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final TextStyle textStyle = isRTL 
        ? SOCMINTTextStyles.arabicBody1 
        : SOCMINTTextStyles.englishBody1;
    final TextStyle labelStyle = isRTL 
        ? SOCMINTTextStyles.arabicBody2 
        : SOCMINTTextStyles.englishBody2;
    
    return TextFormField(
      controller: controller,
      obscureText: obscureText,
      keyboardType: keyboardType,
      validator: validator,
      onChanged: onChanged,
      enabled: enabled,
      maxLines: maxLines,
      minLines: minLines,
      style: textStyle,
      decoration: InputDecoration(
        labelText: label != null ? (isRequired ? '$label *' : label) : null,
        hintText: hint,
        labelStyle: labelStyle,
        prefixIcon: prefixIcon != null ? Icon(prefixIcon) : null,
        suffixIcon: suffix,
      ),
    );
  }
}

/// Alert/notification card with appropriate styling based on type
class SOCMINTAlert extends StatelessWidget {
  final String message;
  final String? title;
  final AlertType type;
  final VoidCallback? onClose;

  const SOCMINTAlert({
    Key? key,
    required this.message,
    this.title,
    this.type = AlertType.info,
    this.onClose,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    
    // Determine colors based on type
    Color backgroundColor;
    Color borderColor;
    Color iconColor;
    IconData icon;
    
    switch (type) {
      case AlertType.success:
        backgroundColor = SOCMINTColors.success.withOpacity(0.1);
        borderColor = SOCMINTColors.success;
        iconColor = SOCMINTColors.success;
        icon = Icons.check_circle;
        break;
      case AlertType.warning:
        backgroundColor = SOCMINTColors.warning.withOpacity(0.1);
        borderColor = SOCMINTColors.warning;
        iconColor = SOCMINTColors.warning;
        icon = Icons.warning;
        break;
      case AlertType.error:
        backgroundColor = SOCMINTColors.uaeRed.withOpacity(0.1);
        borderColor = SOCMINTColors.uaeRed;
        iconColor = SOCMINTColors.uaeRed;
        icon = Icons.error;
        break;
      case AlertType.info:
      default:
        backgroundColor = SOCMINTColors.info.withOpacity(0.1);
        borderColor = SOCMINTColors.info;
        iconColor = SOCMINTColors.info;
        icon = Icons.info;
        break;
    }
    
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: backgroundColor,
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: borderColor),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (!isRTL) Icon(icon, color: iconColor, size: 24),
          if (!isRTL) const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (title != null) ...[  
                  Text(
                    title!,
                    style: (isRTL ? SOCMINTTextStyles.arabicH4 : SOCMINTTextStyles.englishH4).copyWith(
                      color: Theme.of(context).colorScheme.onSurface,
                    ),
                  ),
                  const SizedBox(height: 4),
                ],
                Text(
                  message,
                  style: (isRTL ? SOCMINTTextStyles.arabicBody1 : SOCMINTTextStyles.englishBody1).copyWith(
                    color: Theme.of(context).colorScheme.onSurface,
                  ),
                ),
              ],
            ),
          ),
          if (isRTL) const SizedBox(width: 16),
          if (isRTL) Icon(icon, color: iconColor, size: 24),
          if (onClose != null) ...[  
            const SizedBox(width: 8),
            IconButton(
              icon: const Icon(Icons.close, size: 18),
              onPressed: onClose,
              padding: EdgeInsets.zero,
              constraints: const BoxConstraints(),
              color: Theme.of(context).colorScheme.onSurface.withOpacity(0.6),
            ),
          ],
        ],
      ),
    );
  }
}

/// Alert types for the SOCMINTAlert widget
enum AlertType {
  info,
  success,
  warning,
  error,
}

/// Section header with consistent styling
class SOCMINTSectionHeader extends StatelessWidget {
  final String title;
  final Widget? action;
  
  const SOCMINTSectionHeader({
    Key? key,
    required this.title,
    this.action,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final TextStyle textStyle = isRTL 
        ? SOCMINTTextStyles.arabicH3 
        : SOCMINTTextStyles.englishH3;
    
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
            style: textStyle.copyWith(
              color: Theme.of(context).colorScheme.onBackground,
            ),
          ),
          if (action != null) action!,
        ],
      ),
    );
  }
}

/// Avatar with SOCMINT styling
class SOCMINTAvatar extends StatelessWidget {
  final String? imageUrl;
  final String? initials;
  final double size;
  final Color? backgroundColor;
  
  const SOCMINTAvatar({
    Key? key,
    this.imageUrl,
    this.initials,
    this.size = 40,
    this.backgroundColor,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        color: backgroundColor ?? SOCMINTColors.rhalGreen,
        image: imageUrl != null
            ? DecorationImage(
                image: NetworkImage(imageUrl!),
                fit: BoxFit.cover,
              )
            : null,
      ),
      child: imageUrl == null && initials != null
          ? Center(
              child: Text(
                initials!,
                style: TextStyle(
                  color: SOCMINTColors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: size * 0.4,
                ),
              ),
            )
          : null,
    );
  }
}

/// Badge with SOCMINT styling
class SOCMINTBadge extends StatelessWidget {
  final String text;
  final Color? color;
  final double fontSize;
  
  const SOCMINTBadge({
    Key? key,
    required this.text,
    this.color,
    this.fontSize = 12,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    final Color badgeColor = color ?? SOCMINTColors.rhalGreen;
    
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: badgeColor.withOpacity(0.1),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: badgeColor),
      ),
      child: Text(
        text,
        style: (isRTL ? SOCMINTTextStyles.arabicCaption : SOCMINTTextStyles.englishCaption).copyWith(
          color: badgeColor,
          fontSize: fontSize,
        ),
      ),
    );
  }
}

/// Divider with SOCMINT styling
class SOCMINTDivider extends StatelessWidget {
  final double height;
  final double thickness;
  final double indent;
  final double endIndent;
  
  const SOCMINTDivider({
    Key? key,
    this.height = 1,
    this.thickness = 1,
    this.indent = 0,
    this.endIndent = 0,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Divider(
      height: height,
      thickness: thickness,
      indent: indent,
      endIndent: endIndent,
      color: Theme.of(context).dividerTheme.color,
    );
  }
}

/// Empty state widget with SOCMINT styling
class SOCMINTEmptyState extends StatelessWidget {
  final String message;
  final String? title;
  final IconData icon;
  final Widget? action;
  
  const SOCMINTEmptyState({
    Key? key,
    required this.message,
    this.title,
    this.icon = Icons.inbox,
    this.action,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    final bool isRTL = Directionality.of(context) == TextDirection.rtl;
    
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              size: 64,
              color: Theme.of(context).colorScheme.onBackground.withOpacity(0.3),
            ),
            const SizedBox(height: 16),
            if (title != null) ...[  
              Text(
                title!,
                style: (isRTL ? SOCMINTTextStyles.arabicH3 : SOCMINTTextStyles.englishH3).copyWith(
                  color: Theme.of(context).colorScheme.onBackground,
                ),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 8),
            ],
            Text(
              message,
              style: (isRTL ? SOCMINTTextStyles.arabicBody1 : SOCMINTTextStyles.englishBody1).copyWith(
                color: Theme.of(context).colorScheme.onBackground.withOpacity(0.7),
              ),
              textAlign: TextAlign.center,
            ),
            if (action != null) ...[  
              const SizedBox(height: 24),
              action!,
            ],
          ],
        ),
      ),
    );
  }
}