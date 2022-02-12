module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  plugins: [
    '@typescript-eslint',
  ],
  globals: {
    module: false,
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'airbnb-base',
    'airbnb-typescript/base',
  ],
  rules: {
    '@typescript-eslint/semi': ['error', 'never'],
    'no-irregular-whitespace': 'off',
    '@typescript-eslint/no-this-alias': 'off',
    'no-restricted-syntax': 'off',
    'import/prefer-default-export': 'off',
    '@typescript-eslint/no-use-before-define': 'off',
    'no-param-reassign': 'off',
    'default-case': 'off',
    'max-len': 'off',
    'no-plusplus': 'off',
    'no-continue': 'off',
    'max-classes-per-file': 'off',
    '@typescript-eslint/dot-notation': 'off',
    '@typescript-eslint/no-implied-eval': 'off',
    '@typescript-eslint/no-throw-literal': 'off',
    '@typescript-eslint/return-await': 'off',
  },
}
