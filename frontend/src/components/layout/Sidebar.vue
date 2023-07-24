<template>
    <div class="sidebar-container">
        <a class="sidebar-brand d-flex align-items-center justify-content-center">
            <img class="img-logo" :src="require('@/assets/img/img-logo-2.png')" alt="Logo 2">
        </a>
        <!-- Divider -->
        <hr class="sidebar-divider my-0">
        <li class="nav-item">
            <router-link to="/index" class="nav-link">
                <i class="fa-solid fa-bolt"></i>
                <span>Feed</span>
            </router-link>
        </li>
        <!-- Divider -->
        <hr class="sidebar-divider">
        <li class="nav-item">
            <router-link to="/gallery" class="nav-link">
                <i class="fa-solid fa-image"></i>
                <span>Galeria</span>
            </router-link>
        </li>
        <!-- Divider -->
        <hr class="sidebar-divider">
        <li class="nav-item">
            <a class="nav-link" @click="logout">
                <i class="fa-solid fa-arrow-right-from-bracket"></i>
                <span>Sair</span>
            </a>
        </li>
        <div class="extra-space"></div>
    </div>
</template>
  
<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";

export default {
    methods: {
        async logout() {
            try {
                await api.post("/logout/", { refresh_token: CookieHelper.getCookie("refresh_token") });
            } catch (error) {
                console.error("Erro ao encerrar a sessão do usuário:", error);
            }

            CookieHelper.deleteCookie("token");
            CookieHelper.deleteCookie("refresh_token");
            this.$router.push("/");
        },
        isActiveLink(routeName) {
            return this.activeLink === routeName;
        },
    },
};
</script>
  
<style scoped>
hr {
    margin: 0;
}

.sidebar-container {
    width: 100px;
    height: 100vh;
    background-color: #4732bb;
}

.sidebar {
    list-style: none;
    margin: 0;
    padding: 0;
    background-color: #4732bb;
}

.sidebar-brand {
    padding: 15px;
    text-align: center;
}

.sidebar-brand img {
    max-width: 40px;
}

.nav-item {
    margin: 10px;
}

.nav-item {
    display: flex;
    align-items: center;
    height: 60px;
}

.nav-item.active {
    background-color: #ffffff;
}

.nav-link {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    flex: 1;
    color: #fff;
    text-decoration: none;
    font-size: 14px;
    padding: 10px;
}

.nav-link i {
    margin-bottom: 0.5rem;
}

.nav-link span {
    margin-bottom: 0.25rem;
}

.nav-link:hover {
    color: #9eeaf9;
}

.nav-link i {
    font-size: 20px;
}

.nav-link span {
    font-size: 12px;
}

.nav-link {
    transition: background-color 0.2s ease;
}

.nav-link>* {
    display: block;
}

.nav-link i {
    margin-bottom: 5px;
}

.extra-space {
    flex: 1;
}
</style>
  