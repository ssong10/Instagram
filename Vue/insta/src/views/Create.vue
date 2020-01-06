<template>
  <form method="post" @submit.prevent="articleCreate()" id=article>
      <input type="text" v-model="content" name="content">
      <br>
      <input type="file" name="file" id="file">
      <button type="submit">작성</button>
  </form>
</template>

<script>
import axios from 'axios'
import {mapGetters} from 'vuex'
export default {
  data() {
    return {
      content : ''
    }
  },
  methods:{
    articleCreate() {
      const formData = new FormData()
      var imagefile = document.querySelector('#file');
      formData.append('user',this.user_id)
      formData.append('content',this.content)
      formData.append('image',imagefile.files[0])
      axios.post('http://127.0.0.1:8000/api/v1/create/',formData,this.options)
      .then(response=>{
        console.log(response.data)
        this.$router.push('/')
      })
      .catch(error =>{
        console.log(error)
      })
    }
  },
  computed : {
    ...mapGetters([
      'options',
      'user_id',
      'username'
    ])
  }
}
</script>

<style>

</style>