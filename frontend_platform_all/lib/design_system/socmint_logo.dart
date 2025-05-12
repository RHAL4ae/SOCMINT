import 'package:flutter/material.dart';
import 'socmint_theme.dart';

/// RHAL Logo Widget
/// 
/// A reusable widget that implements the RHAL logo according to the design guidelines.
/// This widget supports different variants, sizes, and can be used consistently
/// across the application.
class RHALLogo extends StatelessWidget {
  /// The height of the logo in pixels
  final double height;
  
  /// Whether to use the reversed color scheme (black on white)
  final bool isReversed;
  
  /// Whether to use monochrome version (all white or all black)
  final bool isMonochrome;
  
  /// Whether to show the background
  final bool showBackground;
  
  /// Whether to include the tagline "عجمان للتقنيات المتقدمة"
  final bool showTagline;
  
  /// Whether to include the English "RHAL" text below the Arabic logo
  final bool showEnglishText;
  
  const RHALLogo({
    super.key,
    this.height = 40,
    this.isReversed = false,
    this.isMonochrome = false,
    this.showBackground = true,
    this.showTagline = false,
    this.showEnglishText = false,
  });
  
  @override
  Widget build(BuildContext context) {
    // Calculate proportions based on height
    final double barHeight = height * 0.2;
    final double textSize = height * 0.6;
    final double taglineSize = height * 0.3;
    final double englishTextSize = height * 0.42; // 70% of Arabic text size
    final double padding = height * 0.5;
    
    // Determine colors based on variant
    final Color textColor = isMonochrome
        ? (Theme.of(context).brightness == Brightness.dark ? Colors.white : Colors.black)
        : (isReversed ? Colors.black : Colors.white);
    
    final Color barColor = isMonochrome
        ? textColor
        : SOCMINTColors.primary;
    
    final Color backgroundColor = isReversed ? Colors.white : Colors.black;
    
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        // Main logo
        Container(
          height: showTagline || showEnglishText ? height : null,
          padding: EdgeInsets.symmetric(horizontal: padding),
          color: showBackground ? backgroundColor : Colors.transparent,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Green bar
              Container(
                height: barHeight,
                color: barColor,
              ),
              SizedBox(height: height * 0.1),
              // Arabic text "رحّال"
              Text(
                'رحّال',
                style: TextStyle(
                  fontFamily: 'NotoKufiArabic',
                  fontSize: textSize,
                  fontWeight: FontWeight.bold,
                  color: textColor,
                ),
                textDirection: TextDirection.rtl,
              ),
            ],
          ),
        ),
        
        // Optional tagline
        if (showTagline) ...[  
          SizedBox(height: height * 0.25),
          Text(
            'عجمان للتقنيات المتقدمة',
            style: TextStyle(
              fontFamily: 'NotoKufiArabic',
              fontSize: taglineSize,
                fontWeight: FontWeight.w500,
              color: textColor,
            ),
            textDirection: TextDirection.rtl,
          ),
        ],
        
        // Optional English text
        if (showEnglishText) ...[  
          SizedBox(height: height * 0.15),
          Text(
            'RHAL',
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: englishTextSize,
              fontWeight: FontWeight.bold,
              color: textColor,
            ),
          ),
        ],
      ],
    );
  }
}

/// Square RHAL Logo Widget (for app icons, favicons, etc.)
class RHALSquareLogo extends StatelessWidget {
  /// The size of the square logo (width and height will be equal)
  final double size;
  
  /// Whether to use the reversed color scheme (black on white)
  final bool isReversed;
  
  /// Whether to use monochrome version (all white or all black)
  final bool isMonochrome;
  
  /// Border radius of the square
  final double borderRadius;
  
  const RHALSquareLogo({
    super.key,
    this.size = 48,
    this.isReversed = false,
    this.isMonochrome = false,
    this.borderRadius = 0,
  });
  
  @override
  Widget build(BuildContext context) {
    // Calculate proportions based on size
    final double barHeight = size * 0.15;
    final double textSize = size * 0.4;
    
    // Determine colors based on variant
    final Color textColor = isMonochrome
        ? (Theme.of(context).brightness == Brightness.dark ? Colors.white : Colors.black)
        : (isReversed ? Colors.black : Colors.white);
    
    final Color barColor = isMonochrome
        ? textColor
        : SOCMINTColors.primary;
    
    final Color backgroundColor = isReversed ? Colors.white : Colors.black;
    
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: backgroundColor,
        borderRadius: BorderRadius.circular(borderRadius),
      ),
      child: Column(
        children: [
          // Green bar
          Container(
            height: barHeight,
            color: barColor,
          ),
          const Spacer(),
          // Arabic text "رحّال"
          Text(
            'رحّال',
            style: TextStyle(
              fontFamily: 'NotoKufiArabic',
              fontSize: textSize,
              fontWeight: FontWeight.bold,
              color: textColor,
            ),
            textDirection: TextDirection.rtl,
          ),
          SizedBox(height: size * 0.15),
        ],
      ),
    );
  }
}

/// RHAL App Icon Widget (for app launcher icons)
class RHALAppIcon extends StatelessWidget {
  /// The size of the app icon (width and height will be equal)
  final double size;
  
  const RHALAppIcon({
    super.key,
    this.size = 48,
  });
  
  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: SOCMINTColors.primary,
        borderRadius: BorderRadius.circular(size * 0.2), // 20% of size for rounded corners
      ),
      child: Center(
        child: RHALSquareLogo(
          size: size * 0.7, // 70% of container size
          isMonochrome: true,
        ),
      ),
    );
  }
}