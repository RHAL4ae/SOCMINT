/**
 * SOCMINT Design System - Web Tokens
 * 
 * This file provides design tokens for web implementation using CSS variables
 * and Tailwind CSS configuration. It ensures consistency between Flutter and web.
 */

// CSS Variables
const cssVariables = `
:root {
  /* Primary Colors */
  --rhal-green: #00A651;
  --rhal-dark: #1A1A1A;
  
  /* Secondary Colors */
  --white: #FFFFFF;
  --light-gray: #F5F5F5;
  --medium-gray: #CCCCCC;
  --dark-gray: #666666;
  
  /* Accent Colors */
  --uae-red: #EF3340;
  --success: #4CAF50;
  --warning: #FFC107;
  --info: #2196F3;
  
  /* Spacing */
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 24px;
  --spacing-6: 32px;
  --spacing-7: 48px;
  --spacing-8: 64px;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  
  /* Font Sizes */
  --font-size-caption: 12px;
  --font-size-body2: 14px;
  --font-size-body1: 16px;
  --font-size-h4: 18px;
  --font-size-h3: 20px;
  --font-size-h2: 24px;
  --font-size-h1: 32px;
  
  /* Font Weights */
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-snug: 1.3;
  --line-height-normal: 1.4;
  --line-height-relaxed: 1.5;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Dark Mode Overrides */
.dark {
  --light-gray: #212121;
  --medium-gray: #333333;
}
`;

// Tailwind Config
const tailwindConfig = {
  theme: {
    extend: {
      colors: {
        'rhal-green': '#00A651',
        'rhal-dark': '#1A1A1A',
        'light-gray': '#F5F5F5',
        'medium-gray': '#CCCCCC',
        'dark-gray': '#666666',
        'uae-red': '#EF3340',
        'success': '#4CAF50',
        'warning': '#FFC107',
        'info': '#2196F3',
      },
      fontFamily: {
        'dubai': ['Dubai', 'Noto Kufi Arabic', 'sans-serif'],
        'montserrat': ['Montserrat', 'Source Sans Pro', 'sans-serif'],
      },
      fontSize: {
        'caption': '12px',
        'body2': '14px',
        'body1': '16px',
        'h4': '18px',
        'h3': '20px',
        'h2': '24px',
        'h1': '32px',
      },
      fontWeight: {
        light: 300,
        regular: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
      },
      lineHeight: {
        tight: 1.2,
        snug: 1.3,
        normal: 1.4,
        relaxed: 1.5,
      },
      spacing: {
        '1': '4px',
        '2': '8px',
        '3': '12px',
        '4': '16px',
        '5': '24px',
        '6': '32px',
        '7': '48px',
        '8': '64px',
      },
      borderRadius: {
        'sm': '4px',
        'md': '8px',
        'lg': '12px',
      },
      boxShadow: {
        'sm': '0 1px 2px rgba(0, 0, 0, 0.05)',
        'md': '0 2px 8px rgba(0, 0, 0, 0.1)',
        'lg': '0 4px 12px rgba(0, 0, 0, 0.15)',
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ['dark', 'dark-hover'],
      textColor: ['dark', 'dark-hover'],
      borderColor: ['dark', 'dark-hover'],
    },
  },
  plugins: [],
};

// Button Classes
const buttonClasses = {
  primary: 'bg-rhal-green text-white font-semibold py-3 px-6 rounded-md hover:bg-opacity-90 transition duration-300',
  secondary: 'bg-transparent text-rhal-green border border-rhal-green font-semibold py-3 px-6 rounded-md hover:bg-rhal-green hover:bg-opacity-10 transition duration-300',
  tertiary: 'bg-transparent text-rhal-green font-semibold py-3 px-4 hover:underline transition duration-300',
};

// Card Classes
const cardClasses = 'bg-white dark:bg-light-gray rounded-lg shadow-md p-4';

// Form Classes
const formClasses = {
  input: 'w-full bg-white dark:bg-light-gray border border-medium-gray rounded-md py-3 px-4 focus:border-rhal-green focus:ring-1 focus:ring-rhal-green outline-none transition duration-300',
  label: 'block text-dark-gray dark:text-medium-gray mb-2 text-body2',
  checkbox: 'h-5 w-5 rounded text-rhal-green focus:ring-rhal-green',
};

// Alert Classes
const alertClasses = {
  base: 'p-4 rounded-md border',
  info: 'bg-info bg-opacity-10 border-info text-dark-gray',
  success: 'bg-success bg-opacity-10 border-success text-dark-gray',
  warning: 'bg-warning bg-opacity-10 border-warning text-dark-gray',
  error: 'bg-uae-red bg-opacity-10 border-uae-red text-dark-gray',
};

// Export all tokens
module.exports = {
  cssVariables,
  tailwindConfig,
  buttonClasses,
  cardClasses,
  formClasses,
  alertClasses,
};