# SOCMINT Visual Identity Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Color System](#color-system)
3. [Typography](#typography)
4. [Components](#components)
5. [Layout](#layout)
6. [Logo Usage](#logo-usage)
7. [Accessibility](#accessibility)
8. [RTL Support](#rtl-support)
9. [Documentation](#documentation)

## Introduction

The SOCMINT Visual Identity System establishes a consistent and professional identity for the RHAL platform. This guide provides comprehensive documentation for implementing and maintaining the visual identity across all interfaces.

## Color System

### Primary Colors
- **Primary Green (#2E7D32)**: Main brand color
- **Accent Red (#D32F2F)**: Emirati flag red for alerts and errors

### Secondary Colors
- **White (#FFFFFF)**: Background and text
- **Black (#000000)**: Text and dark mode
- **Soft Gray (#E0E0E0)**: UI elements and borders

### Usage Guidelines
- Primary green should be used for brand elements and interactive components
- Accent red should only be used for alerts and error states
- Maintain minimum contrast ratios for accessibility

## Typography

### Arabic Typography
- **Primary Font:** Dubai
- **Fallback Font:** Noto Kufi Arabic
- **Font Weights:**
  - Regular (400)
  - Medium (600)
  - Bold (700)

### English Typography
- **Primary Font:** Montserrat
- **Fallback Font:** Source Sans Pro
- **Font Weights:**
  - Regular (400)
  - Medium (600)
  - Bold (700)

### Typography Hierarchy
```css
/* Headings */
.h1 { font-size: 32px; font-weight: 700; }
.h2 { font-size: 24px; font-weight: 600; }
.h3 { font-size: 20px; font-weight: 600; }

/* Body Text */
.body-large { font-size: 16px; }
.body-medium { font-size: 14px; }
.body-small { font-size: 12px; }
```

## Components

### UI Components
- **Buttons**: Rounded corners (8px), primary color hover
- **Cards**: Rounded corners (12px), light shadow
- **Inputs**: Rounded corners (8px), soft gray background
- **Tables**: 12-column grid, consistent spacing
- **Charts**: Consistent color schemes, clear labels

### Component Usage
```dart
// Example button usage
ElevatedButton(
  onPressed: () {},
  child: Text('Action'),
)

// Example card usage
Card(
  child: Padding(
    padding: const EdgeInsets.all(16.0),
    child: Text('Content'),
  ),
)
```

## Layout

### Grid System
- **Columns**: 12-column grid
- **Gutter**: 16px
- **Breakpoints**:
  - Mobile: 320px - 767px
  - Tablet: 768px - 1023px
  - Desktop: 1024px and up

### Spacing
```css
/* Spacing Tokens */
--spacing-x-small: 4px;
--spacing-small: 8px;
--spacing-medium: 16px;
--spacing-large: 24px;
--spacing-x-large: 32px;
```

## Logo Usage

### Logo Variants
- **Primary**: White on black
- **Secondary**: Black on white
- **Favicon**: 512x512, 192x192, 48x48

### Usage Guidelines
- Preserve green bar above "رحّال"
- Maintain aspect ratio
- Minimum size: 128px
- Clear space: 1x letter height
- No distortion, recoloring, or inversion

## Accessibility

### Requirements
- **Text Contrast**: ≥ 4.5:1
- **Font Size**: ≥ 16px
- **Interactive Elements**: ≥ 44px × 44px
- **Keyboard Navigation**: Supported
- **Screen Reader**: Supported

### Color Blind Modes
- Protanopia
- Deuteranopia
- Tritanopia

## RTL Support

### Implementation
- All components must support RTL
- Text direction: RTL (Arabic)
- Layout direction: RTL
- Adjust padding and margins accordingly

## Documentation

### Version Control
- Current Version: 1.0.0
- Last Updated: 2025-05-10

### Updates
- All changes must be documented
- Include rationale for changes
- Maintain changelog

### Contact
For any questions about the visual identity system, please contact the design team.
