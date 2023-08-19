<template>
  <div class="overflow-hidden bg-white shadow sm:rounded-md">
    <ul role="list" class="divide-y divide-gray-200">
      <li v-for="item in items" :key="item.id" class="px-4 py-4 sm:px-6">
        <slot :item="item">{{ item.id  }}</slot>
      </li>
    </ul>
  </div>
</template>

<script setup>
const items = [
  { id: 1 },
  { id: 2 },
  { id: 3 },
  { id: 4 },
  { id: 5 },
  { id: 6 },
  { id: 7 },
  { id: 8 },
  { id: 9 },
  { id: 10}

]
</script>