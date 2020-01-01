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
.login {
  margin-top:30px;
  margin-left:345px;
  margin-right:342px;
}

.image {
  float:left;
  width:450px;
}
.loginform {
    padding:1rem;
    justify-content: center;
    align-items: center;
    float:right;
    border: solid 0.3px #838383af;
    width:350px;
}
</style>