<template>
    <v-app id="app" class="grey lighten-3">
        <navbar/>
        <router-view></router-view>
        <bottom-section></bottom-section>
    </v-app>
</template>

<script>
    import Navbar from '@/components/Navbar';
    import BottomSection from "@/components/BottomSection";

    export default {
        name: 'App',
        components: {
            BottomSection,
            Navbar
        }
    }
</script>

<style>
  body {
    margin: 0;
  }

  * {
    box-sizing: border-box;
  }
</style>
