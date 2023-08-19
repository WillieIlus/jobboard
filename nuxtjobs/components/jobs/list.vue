<template>
  <div v-if="loading">
    <UiLoading />
  </div>
  <div v-else-if="error">Error: {{ error }}</div>
  <div v-else>
    <div class="py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Job Vacancies</h2>
          <p class="mt-2 text-lg leading-8 text-gray-600">Check out our latest job openings.</p>
        </div>
        <UiBasicCard v-for="job in jobs" :key="job.id">

          <div class="w-full flex flex-col sm:flex-row gap-3 sm:items-center  justify-between overflow-hidden">
            <div>
              <span class="text-purple-800 text-sm">{{ job.category_name }}</span>
              <h3 class="font-bold mt-px">{{ job.title }}</h3>
              <div class="flex items-center gap-3 mt-2">
                <span class="bg-purple-100 text-purple-700 rounded-full px-3 py-1 text-sm">{{ job.job_type }}</span>
                <span class="text-slate-600 text-sm flex gap-1 items-center"> <svg xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                      d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg> {{ job.location_name }}, {{ job.location_country }}</span>
              </div>
            </div>
            <div>
              <button class="bg-indigo-100 text-indigo-700 font-medium px-4 py-2 mb-2 rounded-md flex gap-1 items-center">Apply
                Now
                <EnvelopeIcon class="h-4 w-4" />
              </button>
              <NuxtLink type="button" class="bg-indigo-700 text-white font-medium px-4 py-2 rounded-md flex gap-1 items-center"
              :to="`/jobs/${job.slug}/`">
                More Details
                <ArrowRightIcon class="h-4 w-4" />
              </NuxtLink>
            </div>
          </div>
        </UiBasicCard>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ArrowRightIcon, EnvelopeIcon } from '@heroicons/vue/24/outline';
defineProps(['jobs', 'loading', 'error']);



</script>
