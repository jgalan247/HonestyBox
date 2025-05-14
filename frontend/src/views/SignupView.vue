<template>
  <div class="p-4 max-w-md mx-auto">
    <h2 class="text-xl font-bold mb-2">Sign Up</h2>
    <form @submit.prevent="handleSignup">
      <input v-model="form.username" placeholder="Username" class="input" />
      <input v-model="form.password" type="password" placeholder="Password" class="input mt-2" />
      <input v-model="form.email" placeholder="Email" class="input mt-2" />
      <input v-model="form.lat" placeholder="Latitude" class="input mt-2" />
      <input v-model="form.lon" placeholder="Longitude" class="input mt-2" />
      <button class="btn mt-4">Register</button>
    </form>
    <p class="text-red-500 mt-2" v-if="auth.error">{{ auth.error }}</p>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useAuthStore } from '../stores/authStore'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const form = reactive({
  username: '',
  password: '',
  email: '',
  lat: '',
  lon: ''
})

const handleSignup = async () => {
  await auth.signup(form)
  if (!auth.error) router.push('/login')
}
</script>

