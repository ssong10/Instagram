<template>
  <div class="login">
      <strong><h1>Not Working</h1></strong>

      <h2>로그인</h2>
      <LoginForm/>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
    name: 'Login',
    components: {
        LoginForm
    },
}
</script>

<style>
.login {
    justify-content: center;
    align-items: center;
    border: solid 0.5px ;
}
</style>