<template>
  <BaseLayout>
    <div class="flex justify-center items-center min-h-[70vh]">
      <div class="w-full max-w-md bg-white p-6 rounded shadow-md">
        <h1 class="text-2xl font-bold text-center text-green-800 mb-6">🔐 Login</h1>

        <form @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700">Email</label>
            <input
              v-model="email"
              type="email"
              required
              class="mt-1 block w-full border px-3 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-600"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">Password</label>
            <input
              v-model="password"
              type="password"
              required
              class="mt-1 block w-full border px-3 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-600"
            />
          </div>

          <button
            type="submit"
            class="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 transition"
          >
            Log In
          </button>
        </form>

        <p class="text-sm text-center mt-4">
          Not registered yet?
          <RouterLink to="/signup" class="text-green-700 hover:underline">Sign up here</RouterLink>.
        </p>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseLayout from '@/components/BaseLayout.vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const email = ref('')
const password = ref('')
const router = useRouter()
const authStore = useAuthStore()

async function handleLogin() {
  try {
    await authStore.login(email.value, password.value)
    router.push('/')  // or redirect to dashboard
  } catch (err) {
    alert('Login failed. Please check your credentials.')
  }
}
</script>

