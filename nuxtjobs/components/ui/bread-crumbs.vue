<template>
  <div class="flex justify-center items-center p-24">
    <nav class="flex" aria-label="Breadcrumb">
      <ol role="list" class="flex items-center space-x-4">
        <li>
          <div>
            <a href="#" class="text-white hover:text-blue-100">
              <HomeIcon class="h-5 w-5 flex-shrink-0" aria-hidden="true" />
              <span class="sr-only">Home</span>
            </a>
          </div>
        </li>
        <li v-for="page in pages" :key="page.name">
          <div class="flex items-center">
            <ChevronRightIcon class="h-5 w-5 flex-shrink-0 text-white" aria-hidden="true" />
            <a :href="page.href" class="ml-4 text-sm font-medium text-blue-100 hover:text-blue-200" :aria-current="page.current ? 'page' : undefined">{{ page.name }}</a>
          </div>
        </li>
      </ol>
    </nav>
  </div>
</template>

<script setup>
import { ChevronRightIcon, HomeIcon } from '@heroicons/vue/20/solid'

const pages = [
  { name: 'Projects', href: '#', current: false },
  { name: 'Project Nero', href: '#', current: true },
]
</script>
