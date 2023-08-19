import { defineStore } from "pinia";

const BASE_URL = "http://127.0.0.1:8000";

export const useJobsStore = defineStore("job", {
  id: "job",
  state: () => ({
    job: null,
    loading: true,
    error: null,
    jobs: [],
  }),
  getters: {
    getJob: (state) => state.job,
    isLoading: (state) => state.loading,
    getError: (state) => state.error,
    allJobs: (state) => state.jobs,
    allJobsCount: (state) => state.jobs.length,
  },
  actions: {
    async fetchJob(slug) {
      this.loading = true;
      try {
        const response = await fetch(`${BASE_URL}/jobs/${slug}/`);
        const data = await response.json();
        this.job = data;
      }
      catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchJobs() {
      this.loading = true;
      try {
        const response = await fetch(`${BASE_URL}/jobs/`);
        const data = await response.json();
        this.jobs = data;
      }
      catch (error) {
        this.error = error;
      }
      finally {
        this.loading = false;
      }
    },
    async addJob(job) {
      try {
        const response = await fetch(`${BASE_URL}/jobs/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(job),
        });
        const data = await response.json();
        this.jobs.push(data);
      }
      catch (error) {
        console.error(error);
        this.error = error.message;
      }
    },
  },
});
