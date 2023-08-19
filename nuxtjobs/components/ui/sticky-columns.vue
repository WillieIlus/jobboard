<template>
  <SimpleSearch/>
  <div class="py-6">
    <div class="mx-auto max-w-3xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-12 lg:gap-8 lg:px-8">
      <main class="lg:col-span-9 xl:col-span-8">
        <slot name="main-column">This is the main column</slot>
      </main>
      <aside class="hidden lg:col-span-3 xl:col-span-4 xl:block">
        <div class="sticky top-6 space-y-4">
          <slot name="right-column">This is the right column</slot>
        </div>
      </aside>
    </div>
  </div>
</template>


<script setup>
import SimpleSearch from './simple-search.vue';

const user = {
  name: 'Chelsea Hagon',
  email: 'chelsea.hagon@example.com',
  imageUrl:
    'https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}
const navigation = [
  { name: 'Dashboard', href: '#', current: true },
  { name: 'Calendar', href: '#', current: false },
  { name: 'Teams', href: '#', current: false },
  { name: 'Directory', href: '#', current: false },
]
const userNavigation = [
  { name: 'Your Profile', href: '#' },
  { name: 'Settings', href: '#' },
  { name: 'Sign out', href: '#' },
]
</script>