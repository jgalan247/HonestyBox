<template>
  <BaseLayout>
    <div class="max-w-6xl mx-auto py-10 px-4">
      <h1 class="text-2xl font-bold text-green-800 mb-6">👩‍🌾 Super Admin Dashboard</h1>

      <!-- Toggle -->
      <div class="flex gap-4 mb-6">
        <button
          @click="view = 'pending'"
          :class="view === 'pending' ? activeBtn : inactiveBtn"
        >
          Pending Farmers
        </button>
        <button
          @click="view = 'approved'"
          :class="view === 'approved' ? activeBtn : inactiveBtn"
        >
          Approved Farmers
        </button>
      </div>

      <!-- Pending Farmers -->
      <div v-if="view === 'pending'">
        <h2 class="text-lg font-semibold mb-2">🕓 Pending Accounts</h2>
        <table class="w-full border text-left mb-8">
          <thead class="bg-gray-200">
            <tr>
              <th class="p-2">Name</th>
              <th class="p-2">Email</th>
              <th class="p-2">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="farmer in pendingFarmers" :key="farmer.id" class="border-b">
              <td class="p-2">{{ farmer.name }}</td>
              <td class="p-2">{{ farmer.email }}</td>
              <td class="p-2 flex gap-2">
                <button @click="approveFarmer(farmer.id)" class="bg-green-600 text-white px-3 py-1 rounded">Approve</button>
                <button @click="rejectFarmer(farmer.id)" class="bg-red-600 text-white px-3 py-1 rounded">Reject</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Approved Farmers -->
      <div v-else>
        <h2 class="text-lg font-semibold mb-2">✅ Approved Accounts</h2>
        <table class="w-full border text-left">
          <thead class="bg-gray-200">
            <tr>
              <th class="p-2">Name</th>
              <th class="p-2">Email</th>
              <th class="p-2">Joined</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="farmer in approvedFarmers" :key="farmer.id" class="border-b">
              <td class="p-2">{{ farmer.name }}</td>
              <td class="p-2">{{ farmer.email }}</td>
              <td class="p-2">{{ farmer.joined }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseLayout from '@/components/BaseLayout.vue'

// Mock data (replace with API call)
const view = ref('pending')

const pendingFarmers = ref([
  { id: 1, name: 'Alice Farm', email: 'alice@farm.com' },
  { id: 2, name: 'Greenfield Co.', email: 'green@farm.com' }
])

const approvedFarmers = ref([
  { id: 3, name: 'Sunnydale Farm', email: 'sunny@farm.com', joined: '2024-03-12' }
])

function approveFarmer(id) {
  const farmer = pendingFarmers.value.find(f => f.id === id)
  if (farmer) {
    approvedFarmers.value.push({ ...farmer, joined: new Date().toISOString().split('T')[0] })
    pendingFarmers.value = pendingFarmers.value.filter(f => f.id !== id)
  }
}

function rejectFarmer(id) {
  pendingFarmers.value = pendingFarmers.value.filter(f => f.id !== id)
}

const activeBtn = 'bg-green-700 text-white px-4 py-2 rounded'
const inactiveBtn = 'bg-gray-200 text-gray-700 px-4 py-2 rounded hover:bg-gray-300'
</script>

