<template>
    <v-card class="elevation-3 card-search my-10">
        <v-container class="pa-0">
            <v-row class="ma-0">
                <v-col class="pa-0" cols="7">
                    <v-card-text>
                        <v-text-field
                                solo
                                autofocus
                                hide-details
                                placeholder="Znajdź ogłoszenie...">
                        </v-text-field>
                    </v-card-text >
                </v-col>
                <v-col class="pa-0" cols="3">
                    <v-card-text>
                        <v-text-field
                                solo
                                hide-details
                                placeholder="Gdzie szukasz?">
                        </v-text-field>
                    </v-card-text >
                </v-col>
                <v-col class="py-4" cols="2">
                    <v-btn block large color="blue lighten-3 white--text ">
                        <v-icon left>mdi-magnify</v-icon>
                        <span>Szukaj</span>
                    </v-btn>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
    export default {
        name: "SearchBar"
    }
</script>

<style scoped>
    .card-search {
        background: rgba(255, 255, 255, .8)!important;
    }
</style>
