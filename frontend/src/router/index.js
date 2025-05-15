import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import ProductListView from '../views/ProductListView.vue'
import MapView from '../views/MapView.vue'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'

const routes = [
  { path: '/login', component: LoginView },
  { path: '/signup', component: SignupView },
  { path: '/products', component: ProductListView },
  { path: '/map', component: MapView },
  { path: '/about', component: AboutView },
  { path: '/', component: HomeView } 
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

