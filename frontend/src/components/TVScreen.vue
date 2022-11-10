<template>
<div id="screen">
   <TvWelcomeScreen v-if="showWelcome"></TvWelcomeScreen>
   <TvContents v-if="showContents"></TvContents>
   <TvCurrency v-if="showCurrency"></TvCurrency>
   <TvNews v-if="showNews"></TvNews>
   <TvNotFound v-if="showNotFound"></TvNotFound>
</div>
</template>

<script>
import sourceData from '@/data.json'
import TvContents from '@/components/Pages/TvContents.vue'
import TvCurrency from '@/components/Pages/TvCurrency.vue'
import TvNews from '@/components/Pages/TvNews.vue'
import TvWelcomeScreen from '@/components/Pages/TvWelcomeScreen.vue'
import TvNotFound from '@/components/Pages/TvNotFound.vue'
export default {
  props: {
    id: Number,
    id2:Number
  },
  data () {
return{
  selectedChannelSubpage: 1,
  selectedChannel: null,
  showWelcome: true,
  showContents: false,
  showCurrency: false,
  showNews: false,
  showNotFound:false,
}
    
  },
  name: 'TvScreen',
  created() {
    this.$watch(
      () => this.$route.params,
      () => {
        this.getChannels();
        this.getScreen();
      }
    )
  },
  components: {
    TvContents, TvNews, TvCurrency, TvWelcomeScreen, TvNotFound
  },
  computed: {
    getContent () {
      return sourceData.contents.find(getContent => getContent.id === this.id)
    }
  },
  methods: {
    getChannels(){
      this.selectedChannel = this.$route.params.page;
      this.selectedChannelSubpage = this.$route.params.subpage;
    },
    getScreen() {
      if(this.selectedChannel == 1)
      {
      this.showWelcome= true,
      this.showContents= false,
      this.showCurrency= false,
      this.showNews = false,
      this.showNotFound= false
      }
      else if (this.selectedChannel > 1 &&  this.selectedChannel <= 5)
      {
      this.showWelcome= false,
      this.showContents= true,
      this.showCurrency= false,
      this.showNews = false,
      this.showNotFound= false
      }
      else if (this.selectedChannel >= 6 &&  this.selectedChannel <= 10)
      {
      this.showWelcome= false,
      this.showContents= false,
      this.showCurrency= true,
      this.showNews = false,
      this.showNotFound= false
      }
      else if (this.selectedChannel >= 11 && this.selectedChannel <= 15)
      {
      this.showWelcome= false,
      this.showContents= false,
      this.showCurrency= false,
      this.showNews = true,
      this.showNotFound= false
      }
      else
      {
      this.showWelcome= false,
      this.showContents= false,
      this.showCurrency= false,
      this.showNews = false,
      this.showNotFound= true
      }
    }
  },
  mounted() {
  this.selectedChannel = this.$route.params.page;
  if(this.$route.params.subpage == null)
  {
    this.selectedChannelSubpage = 1
  }
  else
  {
    this.selectedChannelSubpage = this.$route.params.subpage
  }
  this.getScreen();
  }
}
</script>
<style scoped  src="../assets/css/styleHome.css"></style>
