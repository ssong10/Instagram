<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <span v-if="this.$session.get('id')">
        | <router-link to="/about">About</router-link>
      </span>
      <span v-else>
        | <router-link to="/login">Login</router-link>
      </span>
      <div v-if="this.$session.get('id')">
        {{ this.$session.get("id") }} 님 로그인 되었습니다
      </div>
    </div>
    <router-view/>
  </div>
</template>

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
