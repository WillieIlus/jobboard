<template>
  <div class="bg-indigo-50 h-full min-h-screen">
    <div v-if="!user">
      <div class="text-center gap-4">
        <router-link to="/accounts/signup" class="btn bg-green-400  py-4 px-8">Signup</router-link>
        <router-link to="/accounts/login" class="btn bg-cyan-400 py-4 px-8">Login</router-link>
      </div>
    </div>
    <div v-else>
      <div class="text-center">
        <router-link to="/accounts/logout">Logout</router-link>
      </div>
      <div class="text-center">
        <p>Logged in as {{ user.username }}</p>
      </div>
    </div>
    <NuxtPage />
  </div>
</template>
<script setup>
import { useAccountsStore } from '@/store/accounts';

const accountsStore = useAccountsStore();

onMounted(() => {
  accountsStore.initStore();
});

</script>