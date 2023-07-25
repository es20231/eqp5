import { createRouter, createWebHistory } from "vue-router";
import SignIn from "../views/authentication/SignInView.vue";
import authGuard from "./authGuard";

const routes = [
    {
        path: "/",
        name: "sign-in",
        component: SignIn,
    },
    {
        path: "/sign-up",
        name: "sign-up",
        component: () => import("../views/authentication/SignUpView.vue"),
    },
    {
        path: "/forgot-password",
        name: "forgot-password",
        component: () => import("../views/authentication/ForgotPasswordView.vue"),
    },
    {
        path: "/index",
        name: "index",
        component: () => import("../views/IndexView.vue"),
        meta: { requiresAuth: true },
    },
    {
        path: "/gallery",
        name: "gallery",
        component: () => import("../views/pages/GalleryView.vue"),
        meta: { requiresAuth: true },
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

router.beforeEach(authGuard);

export default router;
