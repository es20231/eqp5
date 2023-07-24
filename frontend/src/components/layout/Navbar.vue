<template>
    <div>
        <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">
            <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3" @click="toggleSidebar">
                <i class="fa fa-bars"></i>
            </button>
            <span class="navbar-brand mr-3 d-lg-inline text-gray-600">{{ currentPage }}</span>
            <!-- Topbar Navbar -->
            <div class="topbar-divider d-none d-sm-block"></div>
            <!-- Nav Item - User Information -->
            <div class="ml-auto">
                <span class="mr-2 d-lg-inline text-gray-600">{{ username }}</span>
                <img class="img-profile rounded-circle img-fluid" :src="require('@/assets/img/img-user.png')" />
            </div>
        </nav>
        <!-- Show the Sidebar and Menu component if "show" is true -->
        <div v-if="show" class="menu-container" @click="hideMenu">
            <div class="menu" style="z-index: 9999;">
                <ul>
                    <li><router-link to="/index">Feed</router-link></li>
                    <li><router-link to="/gallery">Galeria</router-link></li>
                </ul>
            </div>
        </div>
    </div>
</template>
  
<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";

export default {
    props: {
        currentPage: String,
    },
    data() {
        return {
            username: "",
            show: false,
        };
    },
    methods: {
        async fetchUserData() {
            try {
                const response = await api.get("/users/me/", {
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                    },
                });
                if (response.status === 200 && response.data.username) {
                    this.username = response.data.username;
                }
            } catch (error) {
                this.username = "erro";
            }
        },
        toggleSidebar() {
            this.show = !this.show;
        },
    },
    created() {
        this.fetchUserData();
    },
};
</script>

<style>
.menu-container {
    position: relative;
}

.menu {
    position: absolute;
    top: 0;
    left: 20px;
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.menu ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.menu li {
    margin-bottom: 10px;
}

.menu li:hover {
    margin-bottom: 10px;
}

.menu a {
    text-decoration: none;
    color: #333;
    display: block;
    padding: 5px 10px;
}

.menu a:hover {
    background-color: #f2f2f2;
}
</style>