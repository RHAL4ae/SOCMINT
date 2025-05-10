/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#2E7D32',
        'accent': '#D32F2F',
        'soft-gray': '#E0E0E0',
      },
      fontFamily: {
        'arabic': ['Dubai', 'Noto Kufi Arabic', 'sans-serif'],
        'english': ['Montserrat', 'Source Sans Pro', 'sans-serif'],
      },
      borderRadius: {
        'card': '12px',
        'button': '8px',
      },
      boxShadow: {
        'card': '0 2px 4px rgba(0, 0, 0, 0.1)',
      },
    },
  },
  plugins: [],
}
