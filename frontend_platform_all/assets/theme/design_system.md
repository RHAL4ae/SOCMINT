# SOCMINT Visual Identity System

## Brand Overview
**Brand Name:** RHAL – عجمان للتقنيات المتقدمة
**Product:** SOCMINT Platform
**Language Support:** Arabic (Primary), English (Secondary)

## Color System

### Primary Colors
- **Primary Green (#2E7D32)**: Main brand color, extracted from logo
- **Accent Red (#D32F2F)**: Emirati flag red for alerts and errors

### Secondary Colors
- **White (#FFFFFF)**: Background and text
- **Black (#000000)**: Text and dark mode
- **Soft Gray (#E0E0E0)**: UI elements and borders

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

## UI Components

### Buttons
- Rounded corners (8px)
- Primary color: Green
- Hover effect: Slight elevation
- Padding: 12px vertical, 24px horizontal

### Cards
- Rounded corners (12px)
- Light shadow
- White background
- Minimum height: 100px

### Layout
- Left sidebar width: 250px
- Top bar height: 64px
- Main content padding: 24px
- Grid columns: 12

## Logo Usage

### Logo Requirements
- Preserve green bar above "رحّال"
- Maintain aspect ratio
- Minimum size: 128px
- Clear space: 1x letter height

### Logo Variants
- Primary: White on black
- Secondary: Black on white
- Favicon: 512x512, 192x192, 48x48

## Brand Assets

### Colors
```css
/* Tailwind CSS */
--primary: #2E7D32;
--accent: #D32F2F;
--soft-gray: #E0E0E0;

/* Flutter */
const Color primaryGreen = Color(0xFF2E7D32);
const Color accentRed = Color(0xFFD32F2F);
```

### Typography
```css
/* Tailwind CSS */
font-arabic: 'Dubai', 'Noto Kufi Arabic', sans-serif;
font-english: 'Montserrat', 'Source Sans Pro', sans-serif;

/* Flutter */
const arabicFont = 'Dubai';
const englishFont = 'Montserrat';
```

## Implementation Guidelines

### RTL Support
- All components must support RTL
- Text direction: RTL (Arabic)
- Layout direction: RTL

### Responsive Design
- Mobile: 320px - 767px
- Tablet: 768px - 1023px
- Desktop: 1024px and up

### Accessibility
- Contrast ratio: ≥ 4.5:1
- Font size: ≥ 16px
- Interactive elements: ≥ 44px × 44px

## Usage Examples

### Button
```html
<button class="bg-primary text-white px-6 py-3 rounded-button hover:shadow-lg">
  Action
</button>
```

### Card
```html
<div class="bg-white rounded-card shadow-card p-4">
  Content
</div>
```

### Text Hierarchy
```html
<h1 class="text-4xl font-bold">Heading 1</h1>
<h2 class="text-3xl font-medium">Heading 2</h2>
<p class="text-lg">Body text</p>
```

## Documentation Updates
Last updated: 2025-05-10

## Contact
For any questions about the design system, please contact the design team.
