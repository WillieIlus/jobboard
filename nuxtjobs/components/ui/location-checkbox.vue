<template>
  <fieldset>
    <legend class="text-lg font-medium text-gray-900">Location</legend>
    <div class="mt-4 divide-y divide-gray-200 border-t border-b border-gray-200">
      <div v-for="(location, locationIdx) in locations" :key="locationIdx" class="relative flex items-start py-4">
        <div class="min-w-0 flex-1 text-sm">
          <label :for="`location-${location.id}`" class="select-none font-medium text-gray-700">{{ location.name }}</label>
        </div>
        <div class="ml-3 flex h-5 items-center">
          <input :id="`location-${location.id}`" :name="`location-${location.id}`" type="radio" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
        </div>
      </div>
    </div>
  </fieldset>
</template>

<script setup>
const locations = [
  { id: 1, name: 'New York' },
  { id: 2, name: 'San Francisco' },
  { id: 3, name: 'Los Angeles' },
  { id: 4, name: 'Chicago' },
  { id: 5, name: 'Seattle' },
];
</script>
