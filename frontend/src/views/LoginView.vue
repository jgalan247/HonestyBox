<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-50 px-4">
    <div class="w-full max-w-md bg-white p-6 rounded-lg shadow-md">
      <h1 class="text-2xl font-bold mb-4 text-green-700 text-center">🔐 Login</h1>

      <form @submit.prevent="handleLogin" class="space-y-3">
        <input v-model="username" type="text" placeholder="Username" class="input" required />
        <input v-model="password" type="password" placeholder="Password" class="input" required />
        <button type="submit" class="btn w-full">Login</button>
      </form>

      <p class="text-red-600 text-sm mt-3 text-center" v-if="auth.error">{{ auth.error }}</p>

      <p class="text-center text-sm text-gray-600 mt-4">
        Don’t have an account?
        <router-link to="/signup" class="text-green-700 font-semibold hover:underline">Sign up</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/authStore'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const auth = useAuthStore()
const router = useRouter()

const handleLogin = async () => {
  await auth.login(username.value, password.value)
  if (auth.token) router.push('/products')
}
</script>

<style scoped>
.input {
  @apply w-full p-2 border border-gray-300 rounded;
}
.btn {
  @apply px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700;
}
</style>

