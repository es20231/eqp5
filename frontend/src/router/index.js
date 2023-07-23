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
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

router.beforeEach(authGuard);

export default router;