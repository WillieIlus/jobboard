<template>
  <LayoutColumns>
    <template #main-column>
      <JobsDetail :job="job" :loading="loading" :error="error" />
    </template>
  </LayoutColumns>
</template>

<script setup>

import { storeToRefs } from 'pinia';
import { useJobsStore } from '~/store/jobs';

const route = useRoute();

const jobsStore = useJobsStore();
const { job, loading, error } = storeToRefs(jobsStore);
const { fetchJob } = jobsStore;

const props = defineProps({
  job: {
    type: Object,
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
  fetchJob(route.params.slug);
});

</script>
