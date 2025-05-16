<template>
  <BaseLayout>
    <div class="max-w-3xl mx-auto py-10 px-4">
      <h1 class="text-2xl font-bold text-green-800 mb-6">📬 Contact Us</h1>

      <p class="mb-6 text-gray-700">
        For general inquiries, support, or feedback about Jersey Honesty Boxes, feel free to reach out using the form below or by email.
      </p>

      <form @submit.prevent="submitForm" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Your Name</label>
          <input v-model="name" type="text" required class="w-full border px-3 py-2 rounded" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Your Email</label>
          <input v-model="email" type="email" required class="w-full border px-3 py-2 rounded" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Message</label>
          <textarea v-model="message" required rows="4" class="w-full border px-3 py-2 rounded"></textarea>
        </div>

        <button type="submit" class="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition">
          Send Message
        </button>
      </form>

      <div v-if="submitted" class="text-green-700 font-semibold mt-4">
        ✅ Thank you! We’ll get back to you shortly.
      </div>

      <hr class="my-8" />

      <div class="text-gray-600">
        <h2 class="font-semibold text-lg mb-2">Our Business</h2>
        <p>Jersey Honesty Boxes<br />St. Helier, Jersey JE2<br />Channel Islands</p>
        <p class="mt-2">Email: <a href="mailto:info@honestybox.je" class="text-green-700 underline">info@honestybox.je</a></p>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseLayout from '@/components/BaseLayout.vue'

const name = ref('')
const email = ref('')
const message = ref('')
const submitted = ref(false)

function submitForm() {
  // Simulate form submission
  submitted.value = true

  // Clear fields after short delay
  setTimeout(() => {
    name.value = ''
    email.value = ''
    message.value = ''
  }, 1000)
}
</script>

