<template>
  <div class="w-full">
    <div class="max-w-6xl mx-auto px-4 pt-6 pb-2">
      <h1 class="text-3xl font-bold text-green-800 mb-4 text-center">🌍 Local Farms & Products</h1>

      <!-- 🔍 Search Box -->
      <div class="mb-4 text-center">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Search for a product (e.g. tomatoes)"
          class="w-full md:w-1/2 p-3 border border-gray-300 rounded shadow-sm"
        />
      </div>
    </div>

    <!-- 🗺️ Map -->
    <l-map
      v-if="filteredFarms.length > 0"
      style="height: calc(100vh - 140px); width: 100%;"
      :zoom="11"
      :center="[49.2, -2.1]"
    >
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; OpenStreetMap contributors"
      />
      <l-marker
        v-for="farm in filteredFarms"
        :key="farm.farmer_id"
        :lat-lng="[parseFloat(farm.lat), parseFloat(farm.lon)]"
      >
        <l-popup>
          <div class="text-sm max-w-[250px]">
            <h3 class="text-base font-bold mb-2 text-green-700">{{ farm.farmer_name }}</h3>

            <div class="flex flex-wrap gap-2">
              <div
                v-for="product in farm.products"
                :key="product.name"
                class="border rounded p-2 w-full sm:w-[115px] bg-white shadow-sm"
              >
                <p class="font-semibold text-sm truncate">{{ product.name }}</p>
                <p v-if="product.description" class="text-xs text-gray-500 truncate italic">
                  {{ product.description }}
                </p>
                <p class="text-xs">💷 {{ product.price }}</p>
                <span
                  class="inline-block mt-1 text-[10px] font-semibold px-2 py-0.5 rounded"
                  :class="product.available === 'yes' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'"
                >
                  {{ product.available === 'yes' ? 'Available' : 'Out of Stock' }}
                </span>
              </div>
            </div>
          </div>
        </l-popup>
      </l-marker>
    </l-map>

    <div v-else class="text-center text-gray-600 mt-6">Loading farms...</div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import {
  LMap,
  LTileLayer,
  LMarker,
  LPopup
} from '@vue-leaflet/vue-leaflet'

const farms = ref([])
const searchTerm = ref('')

const filteredFarms = computed(() => {
  if (!searchTerm.value) return farms.value
  const term = searchTerm.value.toLowerCase()
  return farms.value.filter(farm =>
    farm.products.some(p => p.name.toLowerCase().includes(term))
  )
})

onMounted(async () => {
  try {
    const res = await axios.get('/api/public/farms')
    farms.value = res.data
  } catch (err) {
    console.error('Failed to fetch farms:', err)
  }
})
</script>

<style scoped>
/* Tailwind utility classes handle all styling */
</style>

