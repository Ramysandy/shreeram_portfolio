/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        paper: '#F9F7F2',
        'paper-dark': '#EDE9DF',
        'paper-cream': '#FDF8F3',
        'ink': '#0D0D0D',
        'ink-light': '#2A2A2A',
        'ink-faded': '#4A4A4A',
        'rule': '#1A1A1A',
        'column-bg': '#F2EFE8',
      },
      fontFamily: {
        serif: ['"Playfair Display"', 'Georgia', 'Times New Roman', 'serif'],
        'serif-italic': ['"Playfair Display"', 'Georgia', 'serif'],
        mono: ['"IBM Plex Mono"', '"Courier New"', 'Courier', 'monospace'],
        sans: ['"DM Sans"', 'Helvetica Neue', 'Arial', 'sans-serif'],
        display: ['"Playfair Display SC"', '"Playfair Display"', 'Georgia', 'serif'],
      },
      fontSize: {
        'masthead': ['5rem', { lineHeight: '1', letterSpacing: '-0.02em', fontWeight: '900' }],
        'headline': ['2.5rem', { lineHeight: '1.1', letterSpacing: '-0.01em', fontWeight: '700' }],
        'subhead': ['1.4rem', { lineHeight: '1.3', fontWeight: '600' }],
        'deck': ['1.05rem', { lineHeight: '1.5', fontWeight: '400' }],
        'body-print': ['0.9rem', { lineHeight: '1.65' }],
        'caption': ['0.75rem', { lineHeight: '1.4', letterSpacing: '0.04em' }],
        'classifieds': ['0.78rem', { lineHeight: '1.5' }],
      },
      backgroundImage: {
        'paper-texture': "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E\")",
      },
      borderWidth: {
        '3': '3px',
      },
      boxShadow: {
        'newsprint': '2px 2px 0 rgba(0,0,0,0.08)',
        'newsprint-lg': '4px 4px 0 rgba(0,0,0,0.1)',
        'column': 'inset -1px 0 0 #1A1A1A',
      },
      screens: {
        'print': {'raw': 'print'},
      },
      keyframes: {
        inkBleed: {
          '0%': { letterSpacing: '0', opacity: '0.85' },
          '100%': { letterSpacing: '0.02em', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(8px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideInLeft: {
          '0%': { opacity: '0', transform: 'translateX(-20px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        slideInRight: {
          '0%': { opacity: '0', transform: 'translateX(20px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        stampPulse: {
          '0%, 100%': { transform: 'rotate(-1deg)' },
          '50%': { transform: 'rotate(1deg)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-1000px 0' },
          '100%': { backgroundPosition: '1000px 0' },
        },
      },
      animation: {
        'ink-bleed': 'inkBleed 0.3s ease-out forwards',
        'fade-in': 'fadeIn 0.6s ease-out forwards',
        'slide-in-left': 'slideInLeft 0.5s ease-out forwards',
        'slide-in-right': 'slideInRight 0.5s ease-out forwards',
        'stamp': 'stampPulse 0.5s ease-in-out forwards',
        'shimmer': 'shimmer 3s infinite',
      }
    },
  },
  plugins: [],
};
