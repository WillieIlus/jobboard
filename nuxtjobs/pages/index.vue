<template>
  <div>
    <p class="title">
      Welcome to the Homepage
    </p>
  </div>

  <div>
    <div v-if="user === null">
      <p>You are not logged in.</p>
      <router-link to="/accounts/login">Login</router-link>
    </div>

    <div v-else>
      <p>Username: {{ user.username }}</p>
      <p>Email: {{ user.email }}</p>
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script setup>
import { useAccountsStore } from '@/store/accounts';
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

const accountsStore = useAccountsStore();
const router = useRouter();
const { user } = storeToRefs(accountsStore)

// console.log(user.username);
// console.log(user.password);


const logout = () => {
  accountsStore.logout();
  router.push('/accounts/login'); // Redirect to the login page after logout
};
</script>
