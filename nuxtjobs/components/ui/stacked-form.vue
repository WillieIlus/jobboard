<template>
  <LayoutColumns>
    <template #main-column>
      <form class="bg-white p-7 rounded rounded-xl shadow-xl">
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Post a Job</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">Write all information about the job
              you share.</p>

            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div class="col-span-full">
                <label for="job title" class="block text-sm font-medium leading-6 text-gray-900">Job Title </label>
                <div class="mt-2">
                  <input type="text" name="job title" id="job title" autocomplete="job title" v-model="job.title"
                    class="block w-full rounded-md border-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-2 sm:col-start-1">
                <label for="location" class="block text-sm font-medium leading-6 text-gray-900">Location</label>
                <div class="mt-2">
                  <input type="text" name="location" id="location" autocomplete="Location" v-model="job.location"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-2">
                <label for="job type" class="block text-sm font-medium leading-6 text-gray-900">Job Type</label>
                <div class="mt-2">
                  <input type="text" name="job type" id="job type" autocomplete="job type" v-model="job.job_type"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-2">
                <label for="category" class="block text-sm font-medium leading-6 text-gray-900">Category</label>
                <div class="mt-2">
                  <input type="text" name="category" id="category" autocomplete="category" v-model="job.category"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-2">
                <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Country</label>
                <div class="mt-2">
                  <select id="country" name="country" autocomplete="country-name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Mexico</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-2">
                <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Country</label>
                <div class="mt-2">
                  <select id="country" name="country" autocomplete="country-name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Mexico</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-2">
                <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Country</label>
                <div class="mt-2">
                  <select id="country" name="country" autocomplete="country-name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Mexico</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="col-span-full">
              <label for="job description" class="block text-sm font-medium leading-6 text-gray-900">Description</label>
              <div class="mt-2">
                <textarea id="job description" name="job description" rows="4" v-model="job.description"
                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
              <p class="mt-3 text-sm leading-6 text-gray-600">Write a description about the job.</p>
            </div>

            <div class="col-span-full">
              <label for="cover-photo" class="block text-sm font-medium leading-6 text-gray-900">Poster (optional)</label>
              <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                <div class="text-center">
                  <PhotoIcon class="mx-auto h-12 w-12 text-gray-300" aria-hidden="true" />
                  <div class="mt-4 flex text-sm leading-6 text-gray-600">
                    <label for="file-upload"
                      class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                      <span>Upload a file</span>
                      <input id="file-upload" name="file-upload" type="file" class="sr-only" v-on.change="job.Image" />
                    </label>
                  </div>
                  <p class="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="border-b border-gray-900/10 pb-12">

          <div class="mt-10 space-y-10">
            <fieldset>
              <legend class="text-sm font-semibold leading-6 text-gray-900">paid</legend>
              <div class="mt-6 space-y-6">
                <div class="relative flex gap-x-3">
                  <div class="flex h-6 items-center">
                    <input id="comments" name="comments" type="checkbox"
                      class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="text-sm leading-6">
                    <label for="comments" class="font-medium text-gray-900">active</label>
                  </div>
                </div>
                <div class="relative flex gap-x-3">
                  <div class="flex h-6 items-center">
                    <input id="candidates" name="candidates" type="checkbox"
                      class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="text-sm leading-6">
                    <label for="candidates" class="font-medium text-gray-900">Featured</label>
                  </div>
                </div>
                <div class="relative flex gap-x-3">
                  <div class="flex h-6 items-center">
                    <input id="offers" name="offers" type="checkbox"
                      class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="text-sm leading-6">
                    <label for="offers" class="font-medium text-gray-900">paid</label>
                  </div>
                </div>
              </div>
            </fieldset>
            <fieldset>
              <div class="mt-6 space-y-6">
                <div class="flex items-center gap-x-3">
                  <input id="push-everything" name="push-notifications" type="radio"
                    class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  Paid Amount
                  <label for="push-everything" class="block text-sm font-medium leading-6 text-gray-900">1000</label>
                </div>
                <div class="flex items-center gap-x-3">
                  <input id="push-email" name="push-notifications" type="radio"
                    class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  <label for="push-email" class="block text-sm font-medium leading-6 text-gray-900">10000</label>
                </div>
                <div class="flex items-center gap-x-3">
                  <input id="push-nothing" name="push-notifications" type="radio"
                    class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  <label for="push-nothing" class="block text-sm font-medium leading-6 text-gray-900">100000</label>
                </div>
              </div>
            </fieldset>
          </div>
        </div>

        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit"
            class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </form>
    </template>
    <template #right-column>
      <div class="flex flex-col items-center jusity-center">
        <div class="col-span-full">
          {{ job.title }}
        </div>
        <div class="col-span-2">
          {{ job.location }}
        </div>
        <div class="col-span-2">
          {{ job.job_type }}
        </div>
        <div class="col-span-2">
          {{ job.category }}
        </div>
        <div class="col-span-full">
          {{ job.description }}
        </div>
        <div class="col-span-full">
          {{ job.Image }}
        </div>
        <div class="col-span-full">
          {{ job.active }}
        </div>
        <div class="col-span-full">
          {{ job.featured }}
        </div>
        <div class="col-span-full">
          {{ job.paid }}
        </div>
        <div class="col-span-full">
          {{ job.paid_amount }}
        </div>
        <div class="col-span-full">
          {{ job.phone_number }}
        </div>
        <div class="col-span-full">
          {{ job.email }}
        </div>
        <div class="col-span-full">
          {{ job.openings }}
        </div>

      </div>
    </template>
  </LayoutColumns>
</template>
<script setup>
import { PhotoIcon, UserCircleIcon } from '@heroicons/vue/24/solid'

const about = ref('')

const job = ref({
  title: 'Senior Frontend Developer',
  slug: 'senior-frontend-developer',
  company: 'Workcation',
  description: 'Workcation is a property rental website. We provide property owners with a platform to rent their properties for vacationers.',
  experience: 5,
  salary: 100000,
  location: 'Remote',
  job_type: 'Full Time',
  category: 'Engineering',
  address: '123 Fake St.',
  Image: 'https://example.com/image.jpg',
  active: true,
  featured: true,
  paid: true,
  paid_amount: 100,
  phone_number: '555-555-5555',
  email: 'email@example.com',
  openings: 1,
  last_date: '2021-01-07T19:04:00.000Z',
})

</script>