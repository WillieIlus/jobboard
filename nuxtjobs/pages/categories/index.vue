<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <input v-model="category.name">
      <button type="submit">Add Category</button>
    </form>
  </div>
  <div>
    <div v-if="categories">
      <div v-for="category in categories" index="category.id">
        <NuxtLink :to="`/categories/${category.slug}`">
          {{ category.name }}
        </NuxtLink>
      </div>
    </div>
    <div v-else-if="loading">
      loading ...
    </div>
    <div v-else>
      {{ error }}
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useCategoriesStore } from '@/store/categories'

const categoriesStore = useCategoriesStore()
const { categories, loading, error } = storeToRefs(categoriesStore)
const { fetchCategories } = categoriesStore;

const category = ref({
  name: '',
})

const handleSubmit = async () => {
  error.value = []
  await categoriesStore.addCategory(category.value)

  category.value.name = ''
};

onMounted(() => {
  fetchCategories();
});

</script>