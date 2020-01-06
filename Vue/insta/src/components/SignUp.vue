<template>
<div>
        <strong><h1 class="status"></h1></strong>
        <h2>회원가입</h2>
  <!-- <form class="login-form" @submit.prevent="login">
          form에 이벤트 리스너 달아서,
          1) 사용자 입력값 출력
          2) /api-token-auth/로 요청 보내서 토큰값 출력
      <input class="LoginInput" v-model="credentials.username" placeholder="전화번호, 사용자 이름 또는 이메일" type="text" id="nickname"><br>
      <input class="LoginInput" v-model="credentials.password" placeholder="비밀번호" type="password" name="" id="password"><br>
      
  </form> -->
  <form @submit.prevent="signup" class="login-form">
      <input class="LoginInput" v-model="email" placeholder="이메일 주소" required>
      <input class="LoginInput" v-model="name" placeholder="성명" required>
      <input class="LoginInput" v-model="username" placeholder="사용자 이름" required>
      <p class='font-weight-bold' style='color:#D32F2F;' v-for="error in errormessage.username" :key="error">{{ error }}</p>
      <input class="LoginInput" v-model="password" placeholder="비밀번호" required type="password">
      <p class='font-weight-bold' style='color:#D32F2F;' v-for="error in errormessage.password" :key="error">{{ error }}</p>
      <button class="btn-primary" type="submit">가입</button>
    </form>
  </div>

</template>

<script>
import axios from 'axios'
import {mapGetters} from 'vuex'
import router from '../router'
export default {
    name: 'signup',
    data() {
        return {
            signUpUser: {},
            email : '',
            name : '',
            username : '',
            password : '',
            errormessage : {username: [], password: []}
        }
    },
    methods: {
        signup() {
            this.signUpUser ={
                'email' : this.email,
                'name' : this.name,
                'username' : this.username,
                'password' : this.password,
            }
            console.log(this.signUpUser)
            axios.post('http://127.0.0.1:8000/api/v1/accounts/signup/', this.signUpUser)
                .then(() => {
                    this.errormessage = {username: [], password: []}
                    router.push({name:'home'})
                })
                .catch(error => {
                    console.log(error)
                    this.errormessage.username = error.response.data.username
                    this.errormessage.password = error.response.data.password
                })
                this.signUpUser = {}
        },
        clear() {
            this.credentials.username = ''
            this.credentials.password = ''
        },
    },

  computed : {
    ...mapGetters([
      'options',
      'user'
    ])
  }
}
</script>

<style>
.LoginInput {
    font-size:10px;
    width : 70%;
    height :1.5rem;
    margin-bottom : 5px;
    background-color : #f5f5f5;
    border-width : 0.5px;
}
.btn-primary {
    width : 70%;
    color : white;
    background-color : #1097f0;
    border-radius: 2px;
    border-style : none;
}
</style>