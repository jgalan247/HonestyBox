<template>
  <div class="p-4 max-w-md mx-auto">
    <h2 class="text-xl font-bold mb-2">Login</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Username" class="input" />
      <input v-model="password" type="password" placeholder="Password" class="input mt-2" />
      <button class="btn mt-4">Login</button>
    </form>
    <p class="text-red-500 mt-2" v-if="auth.error">{{ auth.error }}</p>
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

