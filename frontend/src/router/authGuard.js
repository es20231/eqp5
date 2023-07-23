import api from "@/config/api";
import Cookies from "js-cookie";

async function isAuthenticated() {
    const token = Cookies.get("token");
    if (!token) {
        return false;
    }

    try {
        const response = await api.post("/login/verify/", { token });
        return response.status === 200;
    } catch (error) {
        return false;
    }
}

export default async function (to, from, next) {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        const authenticated = await isAuthenticated();
        if (authenticated) {
            next();
        } else {
            next({ path: "/" });
        }
    } else {
        next();
    }
}