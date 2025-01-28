/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../**/templates/**/*.html",
    "../**/forms.py",
  ],
  theme: {
    extend: {
      colors: {
        navbar: 'oklch(95.81% 0 0)',
        text_navbar: 'oklch(37.91% 0 0)',
        hover_navbar: 'oklch(83.28% 0 0)',
      },
    },
  },
  plugins: [],
}
