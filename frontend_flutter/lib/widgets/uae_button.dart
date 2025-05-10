import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// A reusable UAE-branded button widget supporting theming, rounded corners, and custom font.
class UAEButton extends StatelessWidget {
  final String label;
  final VoidCallback? onPressed;
  final bool enabled;
  final Color? color;
  final double borderRadius;
  final TextStyle? textStyle;
  final EdgeInsetsGeometry padding;
  final Widget? icon;

  const UAEButton({
    super.key,
    required this.label,
    this.onPressed,
    this.enabled = true,
    this.color,
    this.borderRadius = 12.0,
    this.textStyle,
    this.padding = const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
    this.icon,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final Color effectiveColor = color ?? theme.primaryColor;
    final TextStyle effectiveTextStyle = textStyle ?? GoogleFonts.notoKufiArabic(
      fontWeight: FontWeight.bold,
      color: enabled ? Colors.white : Colors.white70,
      fontSize: 16,
    );
    return ElevatedButton(
      onPressed: enabled ? onPressed : null,
      style: ElevatedButton.styleFrom(
        backgroundColor: enabled ? effectiveColor : effectiveColor.withOpacity(0.6),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(borderRadius),
        ),
        padding: padding,
        elevation: 2,
        textStyle: effectiveTextStyle,
      ),
      child: icon == null
          ? Text(label, style: effectiveTextStyle, textAlign: TextAlign.center)
          : Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                icon!,
                const SizedBox(width: 8),
                Text(label, style: effectiveTextStyle, textAlign: TextAlign.center),
              ],
            ),
    );
  }
}