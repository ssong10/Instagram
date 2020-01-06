<template>
  <div class="login">
      <LoginImage class="image"/>
      <SignUp class="loginform"/>
      <LoginForm class="loginform" />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
import LoginImage from '@/components/LoginImage.vue'
import SignUp from '@/components/SignUp.vue'

export default {
    name: 'Login',
    components: {
        LoginForm,
        LoginImage,
        SignUp,
    },
}
</script>

<style>
.login {
  margin: auto;
  margin-top:30px;
  width:833px;
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