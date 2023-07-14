import { createRouter, createWebHistory } from 'vue-router'

import SingIn from '@/components/SignIn.vue';

const routes = [
  {
    path: '/sign-in',
    name: 'sign-in',
    component: SingIn
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router