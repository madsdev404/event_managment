/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Templates inside apps
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2563EB', // Light: Blue-600
          dark: '#3B82F6',    // Dark: Blue-500
          hover: '#1D4ED8',   // Light: Blue-700
          'dark-hover': '#60A5FA', // Dark: Blue-400
        },
        background: {
          DEFAULT: '#F9FAFB', // Light: Gray-50
          dark: '#0F172A',    // Dark: Slate-900
        },
        surface: {
          DEFAULT: '#FFFFFF', // Light
          dark: '#1E293B',    // Dark: Slate-800
        },
        'text-primary': {
          DEFAULT: '#111827', // Light: Gray-900
          dark: '#F8FAFC',    // Dark: Gray-50
        },
        'text-muted': {
          DEFAULT: '#6B7280', // Light: Gray-500
          dark: '#94A3B8',    // Dark: Slate-400
        },
        border: {
          DEFAULT: '#E5E7EB', // Light: Gray-200
          dark: '#334155',    // Dark: Slate-700
        },
        accent: {
          DEFAULT: '#10B981', // Light: Green-500
          dark: '#34D399',    // Dark: Green-400
        },
        warning: {
          DEFAULT: '#F59E0B', // Light: Amber-500
          dark: '#FBBF24',    // Dark: Amber-400
        },
        error: {
          DEFAULT: '#EF4444', // Light: Red-500
          dark: '#F87171',    // Dark: Red-400
        },
      },
    },
  },
  plugins: [],
};
