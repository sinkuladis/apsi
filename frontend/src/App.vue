<template>
  <div id="app">
    <navbar/>
    <searchbar/>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
import Searchbar from '@/components/Searchbar'

export default {
  name: 'App',
  components: {
    Navbar,
    Searchbar
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
  }

  body {
    margin: 0;
  }
</style>
