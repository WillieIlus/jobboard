<template>
  <a href="#" style="z-index: 4;" @click="scrollToTop" id="back-to-top" class="back-to-top fixed hidden text-lg rounded-full z-10 bottom-5 right-5 h-9 w-9 text-center bg-indigo-600 text-white leading-9">
    <ArrowUpIcon class="w-6 h-6" />
  </a>
</template>

<script setup>
import { ArrowUpIcon } from '@heroicons/vue/24/outline';

function scrollToTop() {
  // Function to scroll to the top of the page
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  });
}
</script>
