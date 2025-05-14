import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import ProductListView from '../views/ProductListView.vue'

const routes = [
  { path: '/login', component: LoginView },
  { path: '/signup', component: SignupView },
  { path: '/products', component: ProductListView }
]

export default createRouter({
  history: createWebHistory(),
  routes
})

