<template>
    <v-container>
        <v-row align-content="center" justify="center">
            <v-col>
                <div class="display-3 blue-grey--text text--darken-3 text-center">
                    <span class="font-weight-light">Olx</span>
                    <span class="font-weight-medium">ample</span>
                </div>
            </v-col>
        </v-row>
        <v-card color="blue" class="px-3">
            <v-row justify="space-between">
                <v-col cols="7">
                    <v-text-field
                            solo
                            flat
                            hide-details
                            placeholder="Znajdź ogłoszenie...">
                    </v-text-field>
                </v-col>
                <v-col cols="3">
                    <v-text-field
                            solo
                            flat
                            hide-details
                            placeholder="Gdzie szukasz?">
                    </v-text-field>
                </v-col>
                <v-col cols="2">
                    <v-btn block large depressed color="blue lighten-2 white--text ">
                        <v-icon left>mdi-magnify</v-icon>
                        <span>Szukaj</span>
                    </v-btn>
                </v-col>
            </v-row>
        </v-card>
    </v-container>
</template>

<script>
    export default {
        name: 'SearchSection'
    }
</script>

<style scoped>
</style>
