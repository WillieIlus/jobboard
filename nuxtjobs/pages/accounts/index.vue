<template>
  <div v-if="user.username === null">
    <h1 class="text-center">You are not logged in</h1>
    <p class="text-center">Please login to view your account</p>
    <div class="text-center">
      <router-link to="/accounts/login" class="btn btn-primary">Login</router-link>
    </div>
  </div>
  <div v-else>
    <h1 class="text-center">Your Account</h1>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <p><strong>Username:</strong> {{ user.username }}</p>
            <p><strong>Email:</strong> {{ user.email }}</p>
            <p><strong>First Name:</strong> {{ user.first_name }}</p>
            <p><strong>Last Name:</strong> {{ user.last_name }}</p>
            <p><strong>Location:</strong> {{ user.location }}</p>
          </div>
        </div>
        <!-- add a signup and login link div  -->
        <div class="text-center mt-3">
          <router-link to="/accounts/logout">Logout</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useAccountsStore } from '@/store/accounts'

const accountsStore = useAccountsStore()
const user = accountsStore.user
</script>
