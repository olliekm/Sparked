/** @type {import('tailwindcss').Config} */
module.exports = {
  // NOTE: Update this to include the paths to all of your component files.
  content: ["./app/**/*.{js,jsx,ts,tsx}", "./components/**/*.{js,jsx,ts,tsx}"],
  presets: [require("nativewind/preset")],
  theme: {
    colors: {
      'primary': "#262626",
      'secondary': "#FAFAFA",
      'accent': "#FFC700",
      'accent2': "#6FD8E9"
    },
    extend: {
      fontFamily: {
        DMSansRegular: ["DMSans-Regular", "sans-serif"],
      },
    },
  },
  plugins: [],
};