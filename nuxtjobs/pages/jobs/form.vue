<template>
  <LayoutColumns>
    <template #main-column>
      <div class="bg-white border p-7 shadow-md rounded-xl">
        <div class="p-4">
          <h1 class="text-3xl font-semibold capitalize">post a job</h1>
          <div class="text-sm text-gray-500">Fill out the form to get started.
            <span>you are sign up as </span>
            <span class="text-indigo-700">user@gmail.com</span>
          </div>
        </div>
        <form @submit.prevent="submitEvent">
          <div class="min-w-full mb-7">
            <FormsInput label="Title" v-model="job.title" />
          </div>
          <div class="min-w-full flex justify-center gap-3 mb-7">
            <div class="form-group flex-auto">
              <FormsSelect label="Location" :options="locationNames" v-model="job.location" />
            </div>
            <div class="form-group flex-auto">
              <FormsSelect label="Job Type" :options="job_type" v-model="job.jobtype" />
            </div>
            <div class="form-group flex-auto">
              <FormsSelect label="Job Category" :options="categoryNames" v-model="job.jobcategory" />
            </div>
          </div>
          <div class="min-w-full flex justify-center gap-3 mb-7">
            <div class="form-group flex-auto">
              <FormsSelect label="Salary" :options="salary" v-model="job.salary" />
            </div>
            <div class="form-group flex-auto">
              <FormsSelect label="Career Level" :options="career" v-model="job.careerlevel" />
            </div>
            <div class="form-group flex-auto">
              <FormsSelect label="Job Experience" :options="experience" v-model="job.jobexperience" />
            </div>
          </div>
          <div class="min-w-full mb-7">
            <label for="cover-photo" class="block text-sm font-medium leading-6 text-gray-700">Poster (optional)</label>
            <div class="mt-2 flex justify-center rounded-lg border border-dashed border-slate-200 px-6 py-10">
              <div class="text-center">
                <PhotoIcon class="mx-auto h-12 w-12 text-gray-300" aria-hidden="true" />
                <div class="mt-4 flex text-sm leading-6 text-gray-600">
                  <label for="file-upload"
                    class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                    <span>Upload a file</span>
                    <input id="file-upload" name="file-upload" type="file" class="sr-only"
                      @change="job.image = $event.target.files[0]" />
                  </label>
                </div>
                <p class="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
              </div>
            </div>
          </div>
          <div class="min-w-full mb-7">
            <FormsTiptap label="Job Description" v-model="content" />
          </div>
          <div class="min-w-full mb-7">
            <FormsInput label="Contact Email" v-model="job.contactemail" />
          </div>
          <div class="min-w-full flex mb-7 gap-4 justify-end">
            <button type="cancel"
              class="bg-rose-700 px-7 py-3 text-white rounded-xl font-semibold hover:bg-rose-900">Cancel</button>
            <button type="submit" onclick.prevent="submitEvent"
              class="bg-indigo-700 px-7 py-3 text-white rounded-xl font-semibold hover:bg-indigo-900">Submit</button>
          </div>
        </form>
      </div>
    </template>
    <template #right-column>
      <UiBasicCard>
        <div class="p-1">
          <h1 class="text-2xl font-semibold capitalize">Your Job</h1>
        </div>
        <div class="min-w-full mb-7 p-3">
          <h2 class="text-lg font-semibold text-gray-700">Title</h2>
          <div class="min-w-full text-gray-400">{{ job.title }}</div>
        </div>
        <div class="min-w-full flex flex-auto gap-3 mb-7">
          <div class="p-3">
            <h2 class="text-lg font-semibold text-gray-700">Location</h2>
            <div class="min-w-full text-gray-400">{{ job.location }}</div>
          </div>
          <div class="p-3">
            <h2 class="text-lg font-semibold text-gray-700">Job Title</h2>
            <div class="min-w-full text-gray-400">{{ job.jobtype }}</div>
          </div>
        </div>
        <div class="min-w-full flex flex-auto gap-3 mb-7">
          <div class="p-3">
            <h2 class="text-lg font-semibold text-gray-700">Job Category</h2>
            <div class="min-w-full text-gray-400">{{ job.jobcategory }}</div>
          </div>

          <div class="p-3">
            <h2 class="text-lg font-semibold text-gray-700">Salary</h2>
            <div class="min-w-full text-gray-400">{{ job.salary }}</div>
          </div>
        </div>
        <div class="min-w-full flex flex-auto gap-3 mb-7">
          <div class="p-3">
            <h2 class="text-lg font-semibold text-gray-700">Career Level</h2>
            <div class="min-w-full text-gray-400">{{ job.careerlevel }}</div>
          </div>

          <div class="p-3">
            <h2 class="text-lg font-semibold text-gray-700">Job Experience</h2>
            <div class="min-w-full text-gray-400">{{ job.jobexperience }}</div>
          </div>
        </div>

        <div class="min-w-full mb-7 p-3">
          <h2 class="text-lg font-semibold text-gray-700">Poster</h2>
          <div class="min-w-full text-gray-400">{{ job.image }}</div>
        </div>

        <div class="min-w-full mb-7 p-3">
          <h2 class="text-lg font-semibold  text-gray-700">Job Description</h2>
          <div class="min-w-full text-gray-400"><div v-html="content"></div></div>
        </div>
        <div class="min-w-full mb-7 p-3">
          <h2 class="text-lg font-semibold text-gray-700">Contact Email</h2>
          <div class="min-w-full text-gray-400">{{ job.contactemail }}</div>
        </div>
      </UiBasicCard>
    </template>
  </LayoutColumns>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useJobsStore } from '~/store/jobs';
import { useCategoriesStore } from '~/store/categories';
import { useLocationsStore } from '~/store/locations';
import { Editor } from '@tiptap/vue-3'

const jobsStore = useJobsStore();
const categoriesStore = useCategoriesStore();
const locationsStore = useLocationsStore();

const { jobs, loading, error } = storeToRefs(jobsStore);
const { categories, categoryNames } = storeToRefs(categoriesStore);
const { locations, locationNames } = storeToRefs(locationsStore);

const { fetchJobs } = jobsStore;
const { fetchCategories } = categoriesStore;
const { fetchLocations } = locationsStore;


const career = [
  'entry level',
  'mid level',
  'senior level'
]

const job_type = [
  'full time',
  'part time',
  'contract',
  'internship',
  'temporary'
]

const salary = [
  'Less than 20,000',
  '20,000 - 40,000',
  '40,000 - 60,000',
  '60,000 - 80,000',
  '80,000 - 100,000',
  'More than 100,000',
];

const experience = [
  '0 years',
  '1 year',
  '2 years',
  '3 years',
  '4 years',
  '5 years',
  '6 years',
  '7 years',
  '8 years',
  '9+ years',
]



const job = ref({
  title: '',
  location: 'taita taveta',
  jobtype: 'full time',
  jobcategory: '',
  salary: '',
  careerlevel: '',
  jobexperience: '',
  image: '',
  description: 'Description',
  contactemail: '',
})

onMounted(() => {
  fetchJobs();
  fetchCategories();
  fetchLocations();

});

const content = ref('')

watch(content, (newValue) => {
  job.value.description = newValue
})

const submitEvent = async () => {
  console.log(job.value.description)
}
</script>

