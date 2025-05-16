<template>
  <BaseLayout>
    <div class="max-w-4xl mx-auto py-10 px-4">
      <h1 class="text-2xl font-bold text-green-800 mb-6">💸 Pricing</h1>

      <p class="text-gray-700 mb-8">
        Jersey Honesty Boxes is currently **free to use** for both farmers and buyers.
        Below is our proposed pricing structure for future upgrades and optional features.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Free Tier -->
        <div class="border rounded p-6 shadow-sm">
          <h2 class="text-lg font-bold text-green-700 mb-2">🌿 Free</h2>
          <p class="text-gray-600 mb-4">Best for individuals starting out</p>
          <ul class="text-sm text-gray-700 space-y-2">
            <li>✅ List up to 5 products</li>
            <li>✅ Appear on the public map</li>
            <li>✅ Super admin support</li>
          </ul>
          <p class="mt-4 font-bold text-xl">£0 / month</p>
        </div>

        <!-- Pro Tier -->
        <div class="border rounded p-6 shadow-md bg-green-50">
          <h2 class="text-lg font-bold text-green-700 mb-2">🌾 Pro</h2>
          <p class="text-gray-600 mb-4">Ideal for active local farmers</p>
          <ul class="text-sm text-gray-700 space-y-2">
            <li>✅ Unlimited products</li>
            <li>✅ Priority map placement</li>
            <li>✅ Analytics dashboard</li>
            <li>✅ Support via email</li>
          </ul>
          <p class="mt-4 font-bold text-xl">£5 / month</p>
        </div>

        <!-- Business Tier -->
        <div class="border rounded p-6 shadow-sm">
          <h2 class="text-lg font-bold text-green-700 mb-2">🚜 Business</h2>
          <p class="text-gray-600 mb-4">For commercial growers and cooperatives</p>
          <ul class="text-sm text-gray-700 space-y-2">
            <li>✅ All Pro features</li>
            <li>✅ Team accounts</li>
            <li>✅ Custom integrations</li>
            <li>✅ Phone & chat support</li>
          </ul>
          <p class="mt-4 font-bold text-xl">£12 / month</p>
        </div>
      </div>
    </div>
  </BaseLayout>
</template>

<script setup>
import BaseLayout from '@/components/BaseLayout.vue'
</script>

