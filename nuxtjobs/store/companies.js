// lets create company store
// with the syntax like of useCategoriesStore

import { defineStore } from 'pinia';

const BASE_URL = 'http://127.0.0.1:8000';

export const useCompaniesStore = defineStore('companies', {
    id: 'companies',
    state: () => ({
        companies: [],
        company: null,
        loading: false,
        error: null,
    }),
    getters: {
        allCompanies: state => state.companies,
        companiesCount: state => state.companies.length,
        getCompany: state => state.company,
        isLoading: state => state.loading,
        getError: state => state.error,
    },
    actions: {
        async fetchCompanies() {
            this.loading = true;
            try {
                const response = await fetch(`${BASE_URL}/companies/`);
                const data = await response.json();
                this.companies = data;
            }
            catch (error) {
                this.error = error;
            }
            finally {
                this.loading = false;
            }
        },
        async fetchCompany(slug) {
            this.loading = true;
            try {
                const response = await fetch(`${BASE_URL}/companies/${slug}/`);
                const data = await response.json();
                this.company = data;
            }
            catch (error) {
                this.error = error;
            }
            finally {
                this.loading = false;
            }
        },
        async addCompany(company) {
            try {
                const response = await fetch(`${BASE_URL}/companies/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(company),
                });
                const data = await response.json();
                this.companies.push(data);
            }
            catch (error) {
                console.error(error);
                this.error = error.message;
            }
        },
    },
});
//# sourceMappingURL=companies.js.map
