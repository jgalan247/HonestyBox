<template>
  <BaseLayout>
    <div class="max-w-4xl mx-auto py-10">
      <h1 class="text-2xl font-bold mb-6 text-green-800">📦 Your Products</h1>

      <div v-if="products.length === 0" class="text-gray-600">No products added yet.</div>

      <div
        v-for="product in products"
        :key="product.id"
        class="bg-white shadow-md rounded p-4 mb-4 border"
      >
        <div v-if="editingId === product.id">
          <!-- Edit Mode -->
          <input v-model="editedName" class="border px-2 py-1 rounded w-full mb-2" />
          <input v-model.number="editedPrice" type="number" step="0.01" class="border px-2 py-1 rounded w-full mb-2" />
          <textarea v-model="editedDescription" class="border px-2 py-1 rounded w-full mb-2"></textarea>

          <div class="flex gap-3">
            <button @click="saveEdit(product.id)" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">Save</button>
            <button @click="cancelEdit" class="bg-gray-300 px-4 py-2 rounded hover:bg-gray-400">Cancel</button>
          </div>
        </div>
        <div v-else>
          <!-- View Mode -->
          <h2 class="text-xl font-semibold">{{ product.name }}</h2>
          <p class="text-sm text-gray-500 mb-1">£{{ product.price.toFixed(2) }}</p>
          <p class="text-gray-700 mb-2">{{ product.description }}</p>
          <div class="flex gap-3">
            <button @click="startEdit(product)" class="bg-yellow-400 text-white px-4 py-2 rounded hover:bg-yellow-500">Edit</button>
            <button @click="deleteProduct(product.id)" class="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseLayout from '@/components/BaseLayout.vue'

// Mock product data (replace with API later)
const products = ref([
  { id: 1, name: 'Fresh Eggs', price: 2.5, description: 'A dozen free-range eggs' },
  { id: 2, name: 'Potatoes', price: 3.0, description: '2kg of Jersey Royals' },
])

const editingId = ref(null)
const editedName = ref('')
const editedPrice = ref(0)
const editedDescription = ref('')

function startEdit(product) {
  editingId.value = product.id
  editedName.value = product.name
  editedPrice.value = product.price
  editedDescription.value = product.description
}

function cancelEdit() {
  editingId.value = null
}

function saveEdit(id) {
  const index = products.value.findIndex(p => p.id === id)
  if (index !== -1) {
    products.value[index].name = editedName.value
    products.value[index].price = editedPrice.value
    products.value[index].description = editedDescription.value
  }
  editingId.value = null
}

function deleteProduct(id) {
  products.value = products.value.filter(p => p.id !== id)
}
</script>

