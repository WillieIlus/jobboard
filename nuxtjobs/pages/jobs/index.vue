<template>
  <JobsList :jobs="jobs" :loading="loading" :error="error" />
  <div v-if="locations">
    <div v-for="location in locations" :key="location.id">
      <h2>{{ location.name }}</h2>
      <div v-for="location in location.jobs" :key="location.id">
        <h3>{{ location.name }}</h3>
        <p>{{ location.description }}</p>
      </div>
    </div>
  </div>
  <div v-if="categories">
    <div v-for="category in categories" :key="category.id">
      <h2>{{ category.name }}</h2>
      <div v-for="job in category.jobs" :key="job.id">
        <h3>{{ job.title }}</h3>
        <p>{{ job.description }}</p>
      </div>
    </div>
  </div>
</template>
<script setup>
import { storeToRefs } from 'pinia';
import { useJobsStore } from '~/store/jobs';
import { useCategoriesStore } from '~/store/categories';
import { useLocationsStore } from '~/store/locations';

const jobsStore = useJobsStore();
const categoriesStore = useCategoriesStore();
const locationsStore = useLocationsStore();

const { jobs, loading, error } = storeToRefs(jobsStore);
const { categories } = storeToRefs(categoriesStore);
const { locations } = storeToRefs(locationsStore);


const { fetchJobs } = jobsStore;
const { fetchCategories } = categoriesStore;
const { fetchLocations } = locationsStore;

const props = defineProps({
  jobs: {
    type: Array,
    required: true,
  },
  categories: {
    type: Array,
    required: true,
  },
  locations: {
    type: Array,
    required: true,
  },
  loading: {
    type: Boolean,
    required: true,
  },
  error: {
    type: String,
    required: true,
  },
});

onMounted(() => {
  fetchJobs();
  fetchCategories();
  fetchLocations();
});

</script>