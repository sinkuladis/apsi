<template>
    <div>
    <v-container class="py-0">
        <v-toolbar flat>
            <!--Toorbar title-->
            <v-toolbar-title>
                <v-card :ripple="false" :to="'/'" class="display-1 blue-grey--text text--darken-3">
                    <span class="font-weight-light">Olx</span>
                    <span class="font-weight-medium">ample</span>
                </v-card>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <!--Account icon button-->
            <!--TODO: Can it be done with only one button?-->
            <div>
                <v-btn v-if="!loggedIn" :to="'/login'" :ripple="false" fab text x-small dark
                       class="me-4 grey lighten-2 blue--text text--darken-1">
                    <v-icon medium>mdi-account</v-icon>
                </v-btn>
                <v-menu v-if="loggedIn" :ripple="false" offset-y>
                    <template v-slot:activator="{ on }">
                        <v-btn fab text x-small dark class="me-4 grey lighten-2 blue--text text--darken-1" v-on="on">
                            <v-icon medium>mdi-account</v-icon>
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
            </div>

            <!--"Dodaj ogłoszenie" button-->
            <v-btn depressed dark color="orange">
                + DODAJ OGŁOSZENIE
            </v-btn>
        </v-toolbar>
    </v-container>
    <v-divider></v-divider>
    </div>
</template>

<script>
    export default {
        name: 'Navbar',
        data() {
            return {
                menuItems: [
                    {title: 'Ogłoszenia'},
                    {title: 'Ustawienia'}
                ],
                loggedIn: false
            }
        }
    }
</script>

<style scoped>
</style>
