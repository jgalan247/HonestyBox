<template>
  <div class="min-h-screen flex flex-col font-sans text-gray-800 bg-gray-50">
    <!-- 🌿 Navigation -->
    <nav class="bg-white shadow-md py-3 sticky top-0 z-50 border-b">
      <div class="max-w-7xl mx-auto px-6 flex justify-between items-center">
        <router-link to="/" class="text-2xl font-bold text-green-700 hover:text-green-800">
          🧺 HonestyBox
        </router-link>

        <div class="space-x-4 flex items-center text-sm font-medium">
          <router-link to="/map" class="text-gray-700 hover:text-green-600">🗺️ Map</router-link>
          <router-link to="/about" class="text-gray-700 hover:text-green-600">ℹ️ About</router-link>

          <router-link v-if="!auth.token" to="/login" class="px-3 py-1 rounded bg-green-600 text-white hover:bg-green-700">
            🔐 Login
          </router-link>
          <router-link v-if="!auth.token" to="/signup" class="px-3 py-1 rounded bg-gray-200 text-gray-800 hover:bg-gray-300">
            ✍️ Sign Up
          </router-link>
          <button v-else @click="logout" class="px-3 py-1 rounded bg-red-100 text-red-700 hover:bg-red-200">
            🚪 Logout
          </button>
        </div>
      </div>
    </nav>

    <!-- 🚀 Main Content -->
    <main class="flex-grow pt-6">
      <router-view />
    </main>

    <!-- 📫 Footer -->
    <footer class="bg-white text-center text-sm text-gray-500 py-4 border-t mt-6">
      © 2025 HonestyBox. All rights reserved.
    </footer>
  </div>
</template>

<script setup>
import { useAuthStore } from './stores/authStore'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const logout = () => {
  auth.logout()
  router.push('/login')
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap');

body {
  font-family: 'Nunito', sans-serif;
}
</style>

