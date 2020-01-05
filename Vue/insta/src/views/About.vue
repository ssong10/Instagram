<template>
    <div class="about">
    <h1>My Page</h1>
    <div v-for="article in articles" :key="article.created_at">
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
    axios.get('http://127.0.0.1:8000/api/v1/create/1/',this.$store.getters.options)
    .then(response => {
      this.articles = response.data
      console.log(this.articles)
    })
  }
}
</script>

<style>

</style>