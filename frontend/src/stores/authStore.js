import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    user: null,
    error: null
  }),
  actions: {
    async login(username, password) {
      try {
        const res = await axios.post('/api/auth/login', { username, password })
        this.token = res.data.access_token
        localStorage.setItem('token', this.token)
        this.error = null
      } catch (err) {
        this.error = 'Login failed'
        this.token = ''
        localStorage.removeItem('token')
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
    }
  }
})

