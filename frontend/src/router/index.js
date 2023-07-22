import { createRouter, createWebHistory } from 'vue-router'
import SignIn from '../views/SignInView.vue';

const routes = [
  {
    path: '/',
    name: 'sign-in',
    component: SignIn
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router