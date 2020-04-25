<template>
    <v-app id="app" class="grey lighten-3">
        <navbar/>
<!--        <search-section/>-->
        <router-view></router-view>
        <bottom-section class="footer"></bottom-section>
    </v-app>
</template>

<script>
    import Navbar from '@/components/Navbar';
    // import SearchSection from '@/components/SearchSection';
    import BottomSection from "@/components/BottomSection";

    export default {
        name: 'App',
        components: {
            BottomSection,
            Navbar,
            // SearchSection
        }
    }
</script>

<style>
</style>
