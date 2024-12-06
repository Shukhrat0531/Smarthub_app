import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Quiz_page from '@/views/Quiz_page.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/quiz",
      name: "quiz",
      component: Quiz_page,
    },
    {
      path: "/category/:id",
      name: "category_detail",
      component: () => import("../views/CategoryDetail.vue"),
      props: true,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/result",
      name: "result",
      component: () => import("../components/ResultView.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../views/RegistrationPage.vue"),
    },
  ],
});

export default router
