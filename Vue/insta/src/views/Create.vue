<template>
  <form method="post" @submit.prevent="articleCreate()" id=article>
      <input type="text" name="content">
      <br>
      <input type="file" name="file" id="file">
      <button type="submit">작성</button>
  </form>
</template>

<script>
import axios from 'axios'
import {mapGetters} from 'vuex'
export default {
  methods:{
    articleCreate() {
      const formData = new FormData()
      formData.append('user',this.user)
      axios.post('http://127.0.0.1:8000/api/v1/create/',formData,this.options)
      .then(response=>{
        console.log(response.data)
      })
      .catch(error =>{
        console.log(error)
      })
    }
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

</style>