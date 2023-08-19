<template>
  <div class="py-10 px-6">
    <div class="max-w-sm mx-auto py-10 px-6">
      <form v-on:submit.prevent="submitForm">
        <input v-model="email" type="email" name="email" placeholder="Your email address..."  class="=">
        <input v-model="username" type="text" name="username" placeholder="Your username"  class="">
        <input v-model="password" type="password" name="password" placeholder="Your password"  class="">
        <input v-model="repeat_password" type="password" name="repeat" placeholder="Repeat" class="">
      
      </form>
    </div>
  </div>
</template>
<script setup>
import { routerKey } from 'vue-router';

let email=ref('')
let password=ref('')
let repeat_password=ref('')
let errors=ref('')

async function submitForm(){
  console.log('submitForm called  ')
  errors.value = []
  await $fetch('http://127.0.0.1:8000/', {
    method: 'POST',
    body:{
      username: username.value,
      email: email.value,
      password: password.value,
      password_confirmation: password_confirmation.value,

    }
  }).then(Response =>{
    console.log('response', Response)
    routerKey.push({ path: '/login'})
  })
  // .catch(error=
}
</script>