<template>
  <BaseLayout>
    <div class="flex justify-center items-center min-h-[70vh]">
      <div class="w-full max-w-lg bg-white p-6 rounded shadow-md">
        <h1 class="text-2xl font-bold text-center text-green-800 mb-4">✍️ Sign Up</h1>

        <p class="text-sm text-gray-600 mb-6">
          Note: You must sign up from your **farm's location**, as your GPS coordinates will be used to place your honesty box on the map.
        </p>

        <form @submit.prevent="handleSignup" class="space-y-4" v-if="!submitted">
          <div>
            <label class="block text-sm font-medium text-gray-700">Name</label>
            <input v-model="name" required class="w-full px-3 py-2 border rounded" />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">Email</label>
            <input v-model="email" type="email" required class="w-full px-3 py-2 border rounded" />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">Password</label>
            <input v-model="password" type="password" required class="w-full px-3 py-2 border rounded" />
          </div>

          <button
            type="submit"
            class="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 transition"
          >
            Create Account
          </button>
        </form>

        <div v-else class="text-center text-green-700 font-semibold mt-4">
          ✅ Your account has been submitted and is pending confirmation.
        </div>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseLayout from '@/components/BaseLayout.vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const name = ref('')
const email = ref('')
const password = ref('')
const submitted = ref(false)
const router = useRouter()

async function handleSignup() {
  try {
    const position = await getCurrentLocation()

    await axios.post('/api/signup', {
      name: name.value,
      email: email.value,
      password: password.value,
      latitude: position.coords.latitude,
      longitude: position.coords.longitude,
    })

    submitted.value = true
  } catch (err) {
    alert('Signup failed. Please try again from your farm’s location.')
  }
}

function getCurrentLocation() {
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(resolve, reject)
  })
}
</script>

