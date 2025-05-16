<template>
  <BaseLayout>
    <div class="max-w-3xl mx-auto py-10 px-4">
      <h1 class="text-2xl font-bold text-green-800 mb-6">❓ Frequently Asked Questions</h1>

      <div v-for="(item, index) in faqs" :key="index" class="border-b">
        <button
          @click="toggle(index)"
          class="w-full flex justify-between items-center py-4 text-left text-green-700 font-semibold"
        >
          <span>{{ item.question }}</span>
          <span class="text-xl">
            {{ activeIndex === index ? '−' : '+' }}
          </span>
        </button>
        <div v-if="activeIndex === index" class="pb-4 text-gray-700">
          {{ item.answer }}
        </div>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseLayout from '@/components/BaseLayout.vue'

const activeIndex = ref(null)

const faqs = ref([
  {
    question: "What is an honesty box?",
    answer: "An honesty box is a self-service farm stall where you can buy local products and leave payment based on trust.",
  },
  {
    question: "How do I sign up as a farmer?",
    answer: "Go to the Signup page while you're at your farm so we can capture your GPS location. Your account will be reviewed before activation.",
  },
  {
    question: "When will my account be approved?",
    answer: "Usually within 24–48 hours by a super admin. You’ll be notified once approved.",
  },
  {
    question: "Is it free to use this service?",
    answer: "Yes, for now it is completely free for both farmers and buyers. Future pricing will be published on the Pricing page.",
  }
])

function toggle(index) {
  activeIndex.value = activeIndex.value === index ? null : index
}
</script>

