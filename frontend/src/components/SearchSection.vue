<template>
    <v-container>
        <v-row align-content="center" justify="center">
            <v-col cols="12" xs="12">
                <div class="display-3 blue-grey--text text--darken-3 text-center">
                    <span class="font-weight-light">Olx</span>
                    <span class="font-weight-medium">ample</span>
                </div>
            </v-col>
        </v-row>
        <v-card color="blue" class="px-3">
            <v-row justify="center">
                <v-col md="7" sm="12">
                    <v-text-field
                            v-model="data.title"
                            solo
                            flat
                            hide-details
                            placeholder="Znajdź ogłoszenie...">
                    </v-text-field>
                </v-col>
                <v-col md="3" sm="12">
                    <v-autocomplete
                            v-model="data.city__name"
                            :items="cities"
                            solo
                            flat
                            hide-details
                            placeholder="Gdzie szukasz?">
                    </v-autocomplete>
                </v-col>
                <v-col md="2" sm="4">
                    <v-btn @click="search"
                           :loading="loading"
                            block large depressed color="blue lighten-2 white--text ">
                        <v-icon left>mdi-magnify</v-icon>
                        <span>Szukaj</span>
                    </v-btn>
                </v-col>
            </v-row>
        </v-card>
        <v-snackbar v-model="snackBar.show" :timeout="2000">
            {{ snackBar.text }}
            <v-btn
                    color="blue"
                    text
                    @click="snackbar = false"
            >
                Close
            </v-btn>
        </v-snackbar>
    </v-container>
</template>

<script>
    export default {
        name: 'SearchSection',
        data() {
            return {
                loading: false,
                data: {
                    "title": '',
                    "city__name": ''
                },
                cities: [
                    'Warszawa', 'Wrocław', 'Toruń', 'Lublin',
                    'Zielona Góra', 'Łódź', 'Kraków',
                    'Opole', 'Rzeszów', 'Białystok', 'Gdańsk',
                    'Katowice', 'Kielce', 'Olsztyn', 'Poznań',
                    'Szczecin'
                ],
                snackBar: {
                    show: false,
                    text: 'Nie mogę znaleźć ogłoszenia'
                }
            }
        },
        methods: {
            search: async function() {
                this.loading=true
                await this.$store.dispatch('searchAdverts', this.data)
                    .then((response) => {
                        if(response.data.length === 0){
                            this.$router.push('/ad-not-found')
                        }
                        this.$router.push('/search')
                    }).catch(() => {
                        this.$router.push('/ad-not-found')
                    })
            }
        }
    }
</script>

<style scoped>
</style>
