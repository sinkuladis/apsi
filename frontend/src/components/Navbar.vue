<template>
    <v-container>
        <v-toolbar flat>
            <v-toolbar-title class="display-1 blue-grey--text text--darken-3">
                <span class="font-weight-light">Olx</span>
                <span class="font-weight-medium">ample</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>
            <div class="text-center">
                <v-menu offset-y>
                    <template v-slot:activator="{ on }">
                        <v-btn icon class="me-2 caption" text color="blue-grey" v-on="on">
                            <v-icon large>mdi-account-circle</v-icon>
                        </v-btn>
                    </template>
                    <v-list subheader>
                        <v-subheader class="blue-grey--text text--darken-3">
                            <span class="font-weight-light">Olx</span>
                            <span class="font-weight-medium">ample</span>
                        </v-subheader>
                        <v-divider></v-divider>
                        <v-list-item
                                v-for="action in menuItems"
                                :key="action.title">
                            <v-list-item-title class="blue--text text--darken-1">
                                {{ action.title }}
                            </v-list-item-title>
                        </v-list-item>
                        <v-list-item class="grey lighten-2 pb-n12">
                            <v-list-item-title class="blue--text text--darken-1">
                                Wyłoguj się
                            </v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
                <v-btn rounded dark color="orange">
                    + DODAJ OGŁOSZENIE
                </v-btn>
            </div>
        </v-toolbar>
    </v-container>
</template>

<script>
    export default {
        name: 'Navbar',
        data() {
            return {
                menuItems: [
                    { title: 'Ogłoszenia' },
                    { title: 'Ustawienia' }
                ]
            }
        }
    }
</script>

<style scoped>
</style>
