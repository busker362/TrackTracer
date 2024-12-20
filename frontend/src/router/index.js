import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Tracks from "@/views/Tracks.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/tracks",
    name: "Tracks",
    component: Tracks,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
