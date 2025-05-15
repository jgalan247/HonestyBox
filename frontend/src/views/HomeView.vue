<template>
  <div class="flex items-center justify-center min-h-screen bg-green-50 px-4">
    <div class="max-w-3xl text-center">
      <h1 class="text-4xl font-bold mb-4 text-green-800">🧺 Welcome to HonestyBox</h1>
      <p class="text-lg text-gray-700 mb-6">
        Discover local farm produce straight from the source. Browse the map, meet local farmers, and buy directly from honesty boxes across Jersey.
      </p>

      <div class="flex flex-col sm:flex-row justify-center gap-4">
        <router-link
          to="/map"
          class="px-6 py-3 bg-green-600 text-white font-semibold rounded hover:bg-green-700 transition"
        >
          🗺️ View Map
        </router-link>
        <router-link
          to="/login"
          class="px-6 py-3 border border-green-600 text-green-700 font-semibold rounded hover:bg-green-600 hover:text-white transition"
        >
          🔐 Login
        </router-link>
        <router-link
          to="/signup"
          class="px-6 py-3 border border-green-600 text-green-700 font-semibold rounded hover:bg-green-600 hover:text-white transition"
        >
          ✍️ Sign Up
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
// No logic needed yet
</script>

<style scoped>
/* Tailwind handles the styles */
</style>

