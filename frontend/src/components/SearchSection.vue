<template>
    <v-card flat class="title-search mb-10 grey lighten-3 text-center">
        <v-container>
            <v-row align-content="center" justify="center">
                <v-col>
                    <div class="display-3 blue-grey--text text--darken-3">
                        <span class="font-weight-light">Olx</span>
                        <span class="font-weight-medium">ample</span>
                    </div>
                    <search-bar></search-bar>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
    import SearchBar from "./SearchBar";

    export default {
        name: 'SearchSection',
        components: {
            SearchBar
        }
    }
</script>

<style scoped>
</style>
