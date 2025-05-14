<template>
  <div class="p-4 max-w-4xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">My Products</h1>

    <div v-if="loading" class="text-gray-500">Loading...</div>
    <div v-else-if="products.length === 0" class="text-gray-500">No products yet.</div>

    <div v-else class="space-y-4">
      <div
        v-for="product in products"
        :key="product.id"
        class="p-4 border rounded shadow-md"
      >
        <h2 class="text-xl font-semibold">{{ product.name }}</h2>
        <p class="text-sm text-gray-600">{{ product.description }}</p>
        <p><strong>Price:</strong> £{{ product.price }}</p>
        <p><strong>Available:</strong> {{ product.available }}</p>
        <p><strong>Location ID:</strong> {{ product.location_id }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/authStore'
import { useRouter } from 'vue-router'

const products = ref([])
const loading = ref(true)
const auth = useAuthStore()
const router = useRouter()

onMounted(async () => {
  if (!auth.token) {
    router.push('/login')
    return
  }

  try {
    const res = await axios.get('/api/farmer/products')
    products.value = res.data
  } catch (err) {
    console.error('Failed to load products:', err)
  } finally {
    loading.value = false
  }
})
</script>

