import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import './assets/css/style.min.css'

createApp(App).use(router).mount('#app')