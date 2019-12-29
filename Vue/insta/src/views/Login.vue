<template>
  <div class="login">
      <LoginImage class="image"/>
      <LoginForm class="loginform" />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import LoginImage from '@/components/LoginImage.vue'

export default {
    name: 'Login',
    components: {
        LoginForm,
        LoginImage
    },
}
</script>

<style>
.image {
  display:inline-block;
}
.loginform {
  display:inline-block;
    padding:1rem;
    justify-content: center;
    align-items: center;
    border: solid 0.3px #838383af;
    width:50%;
}
</style>