module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react-hooks/recommended",
  ],
  ignorePatterns: ["dist", ".eslintrc.cjs"],
  parser: "@typescript-eslint/parser",
  plugins: ["react-refresh"],
  rules: {
    "react-refresh/only-export-components": [
      "warn",
      { allowConstantExport: true },
    ],
    "line-comment-position": ["warn", { position: "above" }],
    "sort-imports": ["warn"],
    "require-await": ["error"],
    radix: ["error"],
    "prefer-template": ["warn"],
    "prefer-spread": ["warn"],
    "prefer-object-spread": ["warn"],
    "prefer-promise-reject-errors": ["warn"],
    "prefer-object-has-own": ["warn"],
    "prefer-numeric-literals": ["warn"],
    "prefer-exponentiation-operator": ["warn"],
    "prefer-destructuring": ["warn"],
    "prefer-const": ["warn"],
    "prefer-arrow-callback": ["warn"],
    "operator-assignment": ["warn"],
    "one-var": ["warn", "never"],
    "object-shorthand": ["warn"],
    "no-with": ["error"],
    "no-var": ["error"],
    "no-void": ["error"],
    "no-useless-return": ["error"],
  },
};
