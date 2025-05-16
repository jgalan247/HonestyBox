// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

// Views
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ProductListView from '@/views/ProductListView.vue'
import AdminDashboard from '@/views/AdminDashboard.vue'
import AboutView from '@/views/AboutView.vue'
import ContactView from '@/views/ContactView.vue'
import PricingView from '@/views/PricingView.vue'
import FAQView from '@/views/FAQView.vue'
import MapView from '@/views/MapView.vue'

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/login', name: 'Login', component: LoginView },
  { path: '/signup', name: 'Signup', component: SignupView },
  { path: '/products', name: 'Products', component: ProductListView, meta: { requiresAuth: true, role: 'farmer' } },
  { path: '/admin', name: 'AdminDashboard', component: AdminDashboard, meta: { requiresAuth: true, role: 'superadmin' } },
  { path: '/about', name: 'About', component: AboutView },
  { path: '/contact', name: 'Contact', component: ContactView },
  { path: '/pricing', name: 'Pricing', component: PricingView },
  { path: '/map', name: 'Map', component: MapView },
  { path: '/faq', name: 'FAQ', component: FAQView },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()

  if (to.meta.requiresAuth) {
    if (!auth.isLoggedIn) {
      return next('/login')
    }

    if (to.meta.role === 'farmer') {
      if (auth.user?.role !== 'farmer' || !auth.user?.confirmed) {
        return next('/')
      }
    }

    if (to.meta.role === 'superadmin') {
      if (auth.user?.role !== 'superadmin') {
        return next('/')
      }
    }
  }

  next()
})

export default router

