// frontend/src/stores/authStore.js
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    user: JSON.parse(localStorage.getItem('user')) || null,
    error: null
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
    isFarmerConfirmed: (state) => state.user?.role === 'farmer' && state.user?.confirmed,
    isSuperAdmin: (state) => state.user?.role === 'superadmin',
  },
  actions: {
    async login(username, password) {
      try {
        const res = await axios.post('/api/auth/login', { username, password })
        this.token = res.data.access_token
        this.user = res.data.user
        localStorage.setItem('token', this.token)
        localStorage.setItem('user', JSON.stringify(this.user))
        this.error = null
      } catch (err) {
        this.error = 'Login failed'
        this.token = ''
        this.user = null
        localStorage.removeItem('token')
        localStorage.removeItem('user')
      }
    },
    async signup(payload) {
      try {
        await axios.post('/api/auth/signup', payload)
        this.error = null
      } catch (err) {
        this.error = 'Signup failed'
      }
    },
    logout() {
      this.token = ''
      this.user = null
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
  }
})

