<template>
  <div class="overflow-hidden bg-white shadow sm:rounded-lg">
    <div class="px-4 py-5 sm:px-6">
      <h3 class="text-lg font-medium leading-6 text-gray-900">Job Description</h3>
      <p class="mt-1 max-w-2xl text-sm text-gray-500">Details about the job position.</p>
    </div>
    <div class="border-t border-gray-200 px-4 py-5 sm:px-6">
      <dl class="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2">
        <div class="sm:col-span-1">
          <dt class="text-sm font-medium text-gray-500">Job Title</dt>
          <dd class="mt-1 text-sm text-gray-900">Backend Developer</dd>
        </div>
        <div class="sm:col-span-1">
          <dt class="text-sm font-medium text-gray-500">Location</dt>
          <dd class="mt-1 text-sm text-gray-900">City, Country</dd>
        </div>
        <div class="sm:col-span-1">
          <dt class="text-sm font-medium text-gray-500">Salary Range</dt>
          <dd class="mt-1 text-sm text-gray-900">$80,000 - $120,000</dd>
        </div>
        <div class="sm:col-span-1">
          <dt class="text-sm font-medium text-gray-500">Job Type</dt>
          <dd class="mt-1 text-sm text-gray-900">Full-time</dd>
        </div>
        <div class="sm:col-span-2">
          <dt class="text-sm font-medium text-gray-500">Responsibilities</dt>
          <dd class="mt-1 text-sm text-gray-900">
            <ul role="list" class="list-disc pl-5 space-y-2">
              <li>Develop and maintain backend services for our web applications.</li>
              <li>Collaborate with the frontend team to design and implement APIs.</li>
              <li>Optimize application performance and scalability.</li>
              <li>Write clean and efficient code with a focus on code quality.</li>
              <li>Debug and fix issues reported by the QA team or customers.</li>
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
            <a href="mailto:jobs@example.com" class="text-indigo-600 hover:text-indigo-500">jobs@example.com</a>.
            We look forward to hearing from you!
          </dd>
        </div>
      </dl>
    </div>
  </div>
</template>
