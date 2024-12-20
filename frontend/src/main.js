import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "@/assets/css/style.css"; // 글로벌 스타일 가져오기

const app = createApp(App);

app.use(router);

app.mount("#app");
