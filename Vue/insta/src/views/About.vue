<template>
    <div class="about">
    <h1>My Page</h1>
    {{article}}
    <div v-for="article in articles" :key="article.created_at">
      <img height="200px" :src="'http://127.0.0.1:8000' + article.image" alt="">
      {{article.content}}
    </div>
    <router-link to="/create">+</router-link>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      articles: ''
    }
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/api/v1/create/` + this.$store.getters.user ,this.$store.getters.options)
    .then(response => {
      this.articles = response.data
      console.log(this.articles)
    })
  }
}
</script>

<style>

</style>