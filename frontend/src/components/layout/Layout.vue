<template>
    <div class="page-top">
        <div id="wrapper">
            <Sidebar v-if="!isSmallScreen" />
            <div id="content-wrapper" class="d-flex flex-column" :style="{
                height: isSmallScreen ? '100vh' : 'auto',
                minHeight: isSmallScreen ? '100vh' : 'inherit',
            }">
                <div id="content">
                    <Navbar :currentPage="currentPage" />
                    <div class="container-fluid">
                        <slot></slot>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Sidebar from "@/components/layout/Sidebar.vue";
import Navbar from "@/components/layout/Navbar.vue";

export default {
    props: {
        currentPage: String,
    },
    components: {
        Sidebar,
        Navbar,
    },
    data() {
        return {
            isSmallScreen: window.innerWidth < 768,
        };
    },
    mounted() {
        window.addEventListener("resize", this.handleResize);
    },
    beforeUnmount() {
        window.removeEventListener("resize", this.handleResize);
    },
    methods: {
        handleResize() {
            this.isSmallScreen = window.innerWidth < 768;
        },
    },
};
</script>
