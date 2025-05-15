<template>
  <div class="p-4 max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-6 text-green-800">🧺 My Products</h1>

    <!-- 🔧 Add New Product Form -->
    <form @submit.prevent="submitNewProduct" class="mb-8 p-4 border rounded bg-gray-50 space-y-4">
      <h2 class="text-xl font-semibold text-gray-700">➕ Add New Product</h2>

      <div>
        <label class="block text-sm font-medium">Name</label>
        <input v-model="form.name" placeholder="e.g. Potatoes" class="input" />
      </div>

      <div>
        <label class="block text-sm font-medium">Description</label>
        <input v-model="form.description" placeholder="e.g. Fresh Royals" class="input" />
      </div>

      <div>
        <label class="block text-sm font-medium">Price</label>
        <div class="flex space-x-2">
          <input
            v-model="form.priceValue"
            type="number"
            step="0.01"
            placeholder="e.g. 2.50"
            class="input w-1/2"
          />
          <select v-model="form.unit" class="input w-1/2">
            <option disabled value="">Select unit</option>
            <option value="per kg">per kg</option>
            <option value="each">each</option>
            <option value="per punnet">per punnet</option>
            <option value="per bunch">per bunch</option>
          </select>
        </div>
      </div>

      <div>
        <label class="block text-sm font-medium">Available</label>
        <select v-model="form.available" class="input">
          <option value="yes">Yes</option>
          <option value="no">No</option>
        </select>
      </div>

      <button class="btn">Add Product</button>
    </form>

    <!-- 🔄 Product List -->
    <h2 class="text-xl font-semibold mb-2 text-gray-700">🧾 Current Products</h2>

    <div v-if="loading" class="text-gray-500">Loading...</div>
    <div v-else-if="products.length === 0" class="text-gray-500">No products yet.</div>

    <div v-else class="grid gap-4">
      <div
        v-for="product in products"
        :key="product.id"
        class="p-4 border rounded shadow-sm bg-white"
      >
        <template v-if="editingId === product.id">
          <input v-model="editForm.name" class="input mb-2" />
          <input v-model="editForm.description" class="input mb-2" />
          <input v-model="editForm.price" class="input mb-2" />
          <select v-model="editForm.available" class="input mb-2">
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
          <div class="flex space-x-2">
            <button @click="saveEdit(product.id)" class="btn bg-blue-600 hover:bg-blue-700">💾 Save</button>
            <button @click="cancelEdit" class="btn bg-gray-500 hover:bg-gray-600">✖ Cancel</button>
          </div>
        </template>
        <template v-else>
          <h3 class="text-lg font-bold text-green-700">{{ product.name }}</h3>
          <p class="text-sm text-gray-600 mb-1"><strong>Description:</strong> {{ product.description }}</p>
          <p><strong>Price:</strong> £{{ product.price }}</p>
          <p><strong>Available:</strong> {{ product.available }}</p>
          <p><strong>Farmer:</strong> {{ product.farmer_name }}</p>
          <p><strong>Location:</strong> {{ product.lat }}, {{ product.lon }}</p>
          <div class="flex space-x-2 mt-2">
            <button @click="startEdit(product)" class="btn bg-yellow-500 hover:bg-yellow-600">📝 Edit</button>
            <button @click="deleteProduct(product.id)" class="btn bg-red-600 hover:bg-red-700">🗑 Delete</button>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/authStore'
import { useRouter } from 'vue-router'

const products = ref([])
const loading = ref(true)
const auth = useAuthStore()
const router = useRouter()

const form = reactive({
  name: '',
  description: '',
  priceValue: '',
  unit: '',
  available: 'yes'
})

const editingId = ref(null)
const editForm = reactive({
  name: '',
  description: '',
  price: '',
  available: ''
})

const fetchProducts = async () => {
  try {
    const res = await axios.get('/api/farmer/products')
    products.value = res.data
  } catch (err) {
    console.error('Failed to load products:', err)
  } finally {
    loading.value = false
  }
}

const submitNewProduct = async () => {
  if (!form.priceValue || !form.unit) {
    alert('Please enter a price and select a unit')
    return
  }

  const payload = {
    name: form.name,
    description: form.description,
    price: `${form.priceValue} ${form.unit}`,
    available: form.available
  }

  try {
    await axios.post('/api/farmer/products', payload)
    await fetchProducts()
    form.name = ''
    form.description = ''
    form.priceValue = ''
    form.unit = ''
    form.available = 'yes'
  } catch (err) {
    console.error('Failed to add product:', err)
  }
}

const startEdit = (product) => {
  editingId.value = product.id
  editForm.name = product.name
  editForm.description = product.description
  editForm.price = product.price
  editForm.available = product.available
}

const cancelEdit = () => {
  editingId.value = null
}

const saveEdit = async (id) => {
  try {
    await axios.put(`/api/farmer/products/${id}`, {
      name: editForm.name,
      description: editForm.description,
      price: editForm.price,
      available: editForm.available
    })
    editingId.value = null
    await fetchProducts()
  } catch (err) {
    console.error('Failed to update product:', err)
  }
}

const deleteProduct = async (id) => {
  if (!confirm('Are you sure you want to delete this product?')) return
  try {
    await axios.delete(`/api/farmer/products/${id}`)
    await fetchProducts()
  } catch (err) {
    console.error('Failed to delete product:', err)
  }
}

onMounted(async () => {
  if (!auth.token) {
    router.push('/login')
    return
  }
  await fetchProducts()
})
</script>

<style scoped>
.input {
  @apply w-full p-2 border rounded mt-1;
}
.btn {
  @apply px-4 py-2 text-white rounded;
}
</style>

