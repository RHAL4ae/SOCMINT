import 'dart:io';
import 'package:flutter/material.dart';
import 'dart:ui' as ui;

void main() async {
  // Create logo files
  await generateLogo('logo_primary.png', Colors.white);
  await generateLogo('logo_white.png', Colors.white);
  await generateLogo('logo_black.png', Colors.black);
  await generateLogo('favicon.png', Colors.green);
}

Future<void> generateLogo(String fileName, Color textColor) async {
  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder);
  final size = Size(128, 128);
  final paint = Paint();

  // Draw green bar
  paint.color = Colors.green;
  canvas.drawRect(Rect.fromLTWH(0, 0, size.width, 20), paint);

  // Draw text
  final textPainter = TextPainter(
    text: TextSpan(
      text: 'رحّال',
      style: TextStyle(
        color: textColor,
        fontSize: 24,
        fontWeight: FontWeight.bold,
      ),
    ),
    textDirection: TextDirection.rtl,
  )..layout();

  final textOffset = Offset(
    (size.width - textPainter.width) / 2,
    (size.height - textPainter.height) / 2,
  );

  textPainter.paint(canvas, textOffset);

  final picture = recorder.endRecording();
  final image = await picture.toImage(size.width.toInt(), size.height.toInt());
  final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
  final pngBytes = byteData!.buffer.asUint8List();

  final file = File('assets/images/logo/$fileName');
  await file.writeAsBytes(pngBytes);
  print('Generated: $fileName');
}
