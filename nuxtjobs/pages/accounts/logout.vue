<template>
  <div>
    <h1 class="text-center">Logout</h1>
    <div class="text-center">
      <button class="btn btn-primary" @click="logout">Logout</button>
    </div>
  </div>
</template>
<script setup>
import { useAccountsStore } from '@/store/accounts'

const router = useRouter()
const accountsStore = useAccountsStore()

const logout = async () => {
  await accountsStore.logout()
  alert('You have been logged out')
  await router.push('/accounts/signup')
}
</script>
```
