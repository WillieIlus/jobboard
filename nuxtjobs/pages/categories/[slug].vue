<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="form.name">
    <input v-model="form.description"> 
    <button type="submit">Add Category</button>
  </form>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useCategoriesStore } from '@/store/categories'

const categoriesStore = useCategoriesStore()
const { categories, loading, error } = storeToRefs(categoriesStore)
const { fetchCategories } = categoriesStore;

const category = ref({
  name: '',
  description: '',
})

const handleSubmit = async () => {
    await categoriesStore.addCategory(category.value)

    category.value.name = ''
    category.value.description = ''
};

onMounted(() => {
  fetchCategories();
});

</script>