import exp from 'constants';
import { defineStore } from 'pinia';

const BASE_URL = 'http://127.0.0.1:8000';

export const useCategoriesStore = defineStore('categories', {
  id: 'categories',
  state: () => ({
    categories: [],
    category: null,
    loading: false,
    error: null,
  }),
  getters: {
    allCategories: state => state.categories,
    categoriesCount: state => state.categories.length,
    getCategory: state => state.category,
    isLoading: state => state.loading,
    getError: state => state.error,
    categoryOptions: state => state.categories.map(category => ({
      name: category.name,
      slug: category.slug,
    })),
    categoryNames: state => state.categories.map(category => category.name),

  },
  actions: {
    async fetchCategories() {
      this.loading = true;
      try {
        const response = await fetch(`${BASE_URL}/categories/`);
        const data = await response.json();
        this.categories = data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchCategory(slug) {
      this.loading = true;
      try {
        const response = await fetch(`${BASE_URL}/categories/${slug}/`);
        const data = await response.json();
        this.category = data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async addCategory(category) {
      try {
        const response = await fetch(`${BASE_URL}/categories/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(category),
        });
        const data = await response.json();
        this.categories.push(data);
      } catch (error) {
        console.error(error);
        this.error = error.message;
      }
    },
    async updateCategory(category) {
      try {
        const response = await fetch(`${BASE_URL}/categories/${category.slug}/`, {
          method: 'PUT',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify(category),
        });
        const data = await response.json();
        const index = this.categories.findIndex(category => category.slug === data.slug);
        this.categories[index] = data;
      } catch (error) {
        console.error(error);
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },
    async deleteCategory(category) {
      try {
        await fetch(`${BASE_URL}/categories/${category.slug}/`, {
          method: 'DELETE',
        });
        this.categories = this.categories.filter(c => c.slug !== category.slug);
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },
  },
});
