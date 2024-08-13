module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: ["synthwave", "cupcake"],
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")]
};
