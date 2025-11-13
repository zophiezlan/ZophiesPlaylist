module.exports = {
  env: {
    browser: true,
    es2021: true,
    jquery: true
  },
  extends: 'eslint:recommended',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  rules: {
    'no-unused-vars': 'warn',
    'no-console': 'off',
    'no-var': 'warn',
    'prefer-const': 'warn',
    'prefer-arrow-callback': 'warn',
    'no-trailing-spaces': 'error',
    'semi': ['error', 'always'],
    'quotes': ['error', 'single', { 'avoidEscape': true }]
  },
  globals: {
    Spotify: 'readonly',
    Raphael: 'readonly',
    _: 'readonly',
    bootstrap: 'readonly'
  }
};
