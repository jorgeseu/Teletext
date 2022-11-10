<template>
      <div id="tv ">
        <div>
             <router-view/>
        </div>
        <div id="selector" class="d-flex justify-content-center ">
          <button v-on:click="IdMinus" class="btn">PREVIOUS</button>
          <button  v-on:click="subpageIdMinus" class="btn"> &lt; </button>
          <button class="btn btn-danger"> </button>
      <button v-on:click="subpageIdPlus" class="btn"> &gt; </button>
      <button v-on:click="IdPlus" class="btn">NEXT</button>
      </div>
      </div>
  </template>
<script>
//import TVScreen from './TVScreen.vue'
export default {
  name: 'TV',
  data () {
    return {
      idscreen: this.$route.params.page,
      isAvaible: true,
      idsubpagescreen:this.$route.params.subpage,
    }
  },
  //components: {
   // TVScreen
  //},
  methods: {
    IdPlus () {
      ++this.idscreen
      this.idsubpagescreen=1
      this.$router.push({ name: 'tvscreen', params: { page: this.idscreen } })
    },
    IdMinus () {
      --this.idscreen
      this.idsubpagescreen=1
      this.$router.push({ name: 'tvscreen', params: { page: this.idscreen } })
    },
    subpageIdPlus () {
      if(this.idsubpagescreen != null)
      {
        ++this.idsubpagescreen
        this.$router.push({ name:'tvscreen.subpage', params: {subpage: this.idsubpagescreen}})
      }
      else
      {
        this.idsubpagescreen=1
        this.$router.push({ name:'tvscreen.subpage', params: {subpage: this.idsubpagescreen}})
      }

    },
    subpageIdMinus ()
    {
      if(this.idsubpagescreen != null)
      {
        --this.idsubpagescreen
        this.$router.push({ name:'tvscreen.subpage', params: {subpage: this.idsubpagescreen}})
      }
      else
      {
        this.idsubpagescreen=1
        this.$router.push({ name:'tvscreen.subpage', params: {subpage: this.idsubpagescreen}})
      }
    }
    },
  computed: {
    getParseId () {
      return parseInt(this.idscreen)
    },
    getParsesubpageId () {
      return parseInt(this.idsubpagescreen)
    }
  },
}
</script>
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped  src="../assets/css/styleHome.css"></style>
