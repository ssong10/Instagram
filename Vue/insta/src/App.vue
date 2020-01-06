<template>
  <div id="app">
    <div id="nav">
      <span v-if="this.$store.state.auth.token">
        <router-link to="/">Home</router-link>
      | <router-link to="/about">About</router-link>
      </span>
      <span v-else>
        <router-link to="/login">Login</router-link>
      </span>
      <div v-if="this.$store.state.auth.token">
        user_id : {{ $store.getters.user_id }} <br>
        {{ $store.getters.username }} 님 로그인 되었습니다
        <button @click="logout" id="logout">logout</button>
      </div>
    </div>
    <router-view/>
  </div>
</template>
<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch('logout').then(() => this.$router.push('/Login'))
    }
  },
  mounted(){
    if (!this.$store.state.auth.token){
      this.$store.dispatch('login',this.$session.get("jwt"))
    }
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
