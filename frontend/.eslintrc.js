module.exports = {
    env: {
      browser: true,
      node: true,
    },
    extends: [
      "plugin:vue/vue3-essential", // Vue 3 기본 규칙
      "eslint:recommended",       // JavaScript 추천 규칙
    ],
    parserOptions: {
      ecmaVersion: 2020,          // 최신 ECMAScript 문법 지원
      requireConfigFile: false,  // Babel 설정 파일 강제 비활성화
    },
    rules: {
      "vue/multi-word-component-names": "off", // 단일 단어 컴포넌트 이름 허용
    },
  };
  