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
  margin-left:250px;
  margin-right:250px;
}

.image {
  float:left;
  width:50%;
  margin-right:20px;
}
.loginform {
    padding:1rem;
    justify-content: center;
    align-items: center;
    float:right;
    border: solid 0.3px #838383af;
    width:40%;
}
</style>