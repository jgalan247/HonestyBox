<template>
  <div class="min-h-screen flex flex-col bg-white text-gray-800">
    <!-- Navbar -->
    <nav class="bg-green-800 text-white shadow">
      <div class="container mx-auto px-4 py-4 flex justify-between items-center">
        <div class="text-xl font-bold">🌿 Jersey Honesty Boxes</div>

        <!-- Mobile Hamburger -->
        <button
          @click="isMobileMenuOpen = !isMobileMenuOpen"
          class="md:hidden text-white text-2xl"
        >
          <span v-if="!isMobileMenuOpen">☰</span>
          <span v-else>✖</span>
        </button>

        <!-- Desktop Navigation -->
        <ul class="hidden md:flex gap-4 text-sm font-medium">
          <li><RouterLink to="/" class="hover:underline">Home</RouterLink></li>
          <li><RouterLink to="/map" class="hover:underline">Map</RouterLink></li>
          <li v-if="!authStore.isLoggedIn"><RouterLink to="/login" class="hover:underline">Login</RouterLink></li>
          <li v-if="!authStore.isLoggedIn"><RouterLink to="/signup" class="hover:underline">Signup</RouterLink></li>
          <li><RouterLink to="/pricing" class="hover:underline">Pricing</RouterLink></li>
          <li v-if="authStore.isFarmerConfirmed"><RouterLink to="/products" class="hover:underline">Products</RouterLink></li>
          <li v-if="authStore.isSuperAdmin"><RouterLink to="/admin" class="hover:underline">Admin</RouterLink></li>
          <li v-if="authStore.isLoggedIn" @click="handleLogout" class="cursor-pointer hover:underline">Logout</li>
        </ul>
      </div>

      <!-- Mobile Menu -->
      <ul
        v-if="isMobileMenuOpen"
        class="md:hidden bg-green-700 px-4 py-3 flex flex-col gap-2 text-sm font-medium"
      >
        <li><RouterLink to="/" class="hover:underline" @click="closeMobile">Home</RouterLink></li>
        <li><RouterLink to="/map" class="hover:underline" @click="closeMobile">Map</RouterLink></li>
        <li v-if="!authStore.isLoggedIn"><RouterLink to="/login" class="hover:underline" @click="closeMobile">Login</RouterLink></li>
        <li v-if="!authStore.isLoggedIn"><RouterLink to="/signup" class="hover:underline" @click="closeMobile">Signup</RouterLink></li>
        <li><RouterLink to="/pricing" class="hover:underline" @click="closeMobile">Pricing</RouterLink></li>
        <li v-if="authStore.isFarmerConfirmed"><RouterLink to="/products" class="hover:underline" @click="closeMobile">Products</RouterLink></li>
        <li v-if="authStore.isSuperAdmin"><RouterLink to="/admin" class="hover:underline" @click="closeMobile">Admin</RouterLink></li>
        <li v-if="authStore.isLoggedIn" @click="handleLogout" class="cursor-pointer hover:underline">Logout</li>
      </ul>
    </nav>

    <!-- Main Content Area -->
    <main class="flex-1 w-full max-w-screen-xl mx-auto px-6 py-6">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-gray-100 border-t py-4 text-center text-sm">
      <RouterLink to="/faq" class="mx-2 hover:underline">FAQ</RouterLink> |
      <RouterLink to="/contact" class="mx-2 hover:underline">Contact</RouterLink> |
      <RouterLink to="/about" class="mx-2 hover:underline">About Us</RouterLink>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const router = useRouter()
const authStore = useAuthStore()
const isMobileMenuOpen = ref(false)

function handleLogout() {
  authStore.logout()
  isMobileMenuOpen.value = false
  router.push('/login')
}

function closeMobile() {
  isMobileMenuOpen.value = false
}
</script>

