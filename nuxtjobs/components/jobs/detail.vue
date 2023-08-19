<template>
  <div v-if="loading">
    <UiLoading />
  </div>
  <div v-else-if="error">Error: {{ error }}</div>
  <div v-else>
    <div class="overflow-hidden bg-white shadow sm:rounded-lg">
      <div class="px-4 py-5 sm:px-6">
        <h3 class="text-lg font-medium leading-6 text-gray-900">Job Description</h3>
        <p class="mt-1 max-w-2xl text-sm text-gray-500">Details about the job position.</p>
      </div>
      <div class="border-t border-gray-200 px-4 py-5 sm:px-6">
        <dl class="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2">
          <div class="sm:col-span-1">
            <dt class="text-sm font-medium text-gray-500">Job Title</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ job.title }}</dd>
          </div>
          <div class="sm:col-span-1">
            <dt class="text-sm font-medium text-gray-500">Location</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ job.location_name }}, job.country_name </dd>
          </div>
          <div class="sm:col-span-1">
            <dt class="text-sm font-medium text-gray-500">Salary Range</dt>
            <dd class="mt-1 text-sm text-gray-900">Ksh {{ job.salary }}</dd>
          </div>
          <div class="sm:col-span-1">
            <dt class="text-sm font-medium text-gray-500">Job Type</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ job.job_type }}</dd>
          </div>
          <div class="sm:col-span-2">
            <dt class="text-sm font-medium text-gray-500">Description</dt>
            <dd class="mt-1 text-sm text-gray-900">
              <ul role="list" class="list-disc pl-5 space-y-2">
                <li>{{ job.Description }}</li>
              </ul>
            </dd>
          </div>
          <div class="sm:col-span-2">
            <dt class="text-sm font-medium text-gray-500">Requirements</dt>
            <dd class="mt-1 text-sm text-gray-900">
              <ul role="list" class="list-disc pl-5 space-y-2">
                <li>Bachelor's degree in Computer Science or related field.</li>
                <li>Proven experience in backend development using JavaScript/Node.js.</li>
                <li>Knowledge of RESTful APIs and web application architecture.</li>
                <li>Experience with databases like MongoDB or PostgreSQL.</li>
                <li>Strong problem-solving and communication skills.</li>
              </ul>
            </dd>
          </div>
          <div class="sm:col-span-2">
            <dt class="text-sm font-medium text-gray-500">How to Apply</dt>
            <dd class="mt-1 text-sm text-gray-900">
              To apply for this position, please send your resume and cover letter to
              <a href="mailto:{{job.email}}" class="text-indigo-600 hover:text-indigo-500">{{ job.email }}</a>.
              We look forward to hearing from you!
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps(['job', 'loading', 'error']);
</script>