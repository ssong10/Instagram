<template>
  <div class="container about">
    <h1>{{ $store.getters.username }}</h1>
    <div class="row">
      <div class="d-inline">
        <img height="100px" width="100px" src="http://127.0.0.1:8000/media/default_image.jpg/" alt="">
      </div>
      <div class="col row">
        <div class="col-4">
          <h3> {{ articles.length }} </h3>
          Post
        </div>
        <div class="col-4">
          <h3> 0 </h3>
          Followers
        </div>
        <div class="col-4">
          <h3> 0 </h3>
          Follwowing
        </div>
      </div>
    </div>
    <div class="row row-cols-3">
      <div class="col" v-for="article in articles" :key="article.created_at">
        <img width="150px" height="150px" :src="'http://127.0.0.1:8000' + article.image" alt="">
      </div>
    </div>

    <router-link style="font-size:30px" to="/create">+</router-link>
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
      axios.get(`http://127.0.0.1:8000/api/v1/create/` + this.$store.getters.user_id, this.$store.getters.options)
        .then(response => {
          this.articles = response.data
          console.log(this.articles)
        })
    }
  }
</script>

<style>

</style>