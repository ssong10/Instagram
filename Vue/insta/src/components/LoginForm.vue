<template>
<div>
        <strong><h1 class="status"></h1></strong>
        <h2>로그인</h2>
  <form class="login-form" @submit.prevent="login">
      <!--  
          form에 이벤트 리스너 달아서,
          1) 사용자 입력값 출력
          2) /api-token-auth/로 요청 보내서 토큰값 출력
      -->
      <input class="LoginInput" v-model="credentials.username" placeholder="전화번호, 사용자 이름 또는 이메일" type="text" id="nickname"><br>
      <input class="LoginInput" v-model="credentials.password" placeholder="비밀번호" type="password" name="" id="password"><br>
      <button class="btn-primary" type="submit">로그인</button>
  </form>
  </div>

</template>

<script>
import axios from 'axios'
// 특정 폴더명으로 경로가 끝나게 되면, 폴더 내부의 indes.js를 뜻함
import router from '../router'
export default {
    name: 'LoginForm',
    data() {
        return {
            credentials: {}
        }
    },
    methods: {
        login() {
            axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
                .then(response => {
                    console.log(response.data.token)
                    const token = response.data.token
                    console.log(token)
                    this.$session.start()
                    this.$session.set('jwt', token)
                    // vuex actions 호출 -> dispatch
                    this.$store.dispatch('login', token)
                    router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })
            this.credentials = []
        }
    },
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