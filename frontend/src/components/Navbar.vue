<template>
    <div>
        <v-container class="py-0">
            <v-toolbar flat>
                <!--Toorbar title-->
                <v-toolbar-title>
                    <v-card :ripple="false" :to="'/'" tag="section"
                            class="display-1 blue-grey--text text--darken-3 white-background">
                        <span class="font-weight-light">Olx</span>
                        <span class="font-weight-medium">ample</span>
                    </v-card>
                </v-toolbar-title>

                <v-spacer></v-spacer>

                <!--Account icon button-->
                <div>
                    <span class="username" v-if="isLoggedIn">{{username}}</span>
                    <v-btn v-if="!isLoggedIn" :to="'/login'" :ripple="false" fab text x-small dark
                        class="me-4 grey lighten-2 blue--text text--darken-1">
                        <v-icon medium>mdi-account</v-icon>
                    </v-btn>
                    <v-menu v-else :ripple="false" offset-y>
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
                                    :key="action.title"
                                    :to="action.to"
                            >
                                <v-list-item-title class="blue--text text--darken-1">
                                    {{ action.title }}
                                </v-list-item-title>
                            </v-list-item>
                            <v-list-item v-on:click="logout" class="grey lighten-2 pb-n12">
                                <v-list-item-title class="blue--text text--darken-1">
                                    Wyloguj się
                                </v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </div>

                <!--"Dodaj ogłoszenie" button-->
                <v-btn :to="advertRedirect" depressed dark color="orange">
                    + DODAJ OGŁOSZENIE
                </v-btn>
            </v-toolbar>
            <v-divider></v-divider>
        </v-container>
    </div>
</template>

<script>
    export default {
        name: 'Navbar',
        computed: {
            isLoggedIn: function() {
                return this.$store.getters.isLoggedIn
            },
            username: function() {
                return this.$store.getters.user.username
            },
            advertRedirect: function() {
                return this.isLoggedIn ? "/submit-advert" : "/login"
            },
            menuItems: function() {
                return [
                    {title: 'Ogłoszenia', to: `/user/${this.$store.getters.user.id}/ads`},
                    {title: 'Obserwowane', to: `/user/${this.$store.getters.user.id}/observed-ads`},
                    {title: 'Ustawienia', to: '/userpage'}
                ]
            }
        },
        methods: {
          logout: async function () {
            await this.$store.dispatch('logout')
          },
        }
    }
</script>

<style scoped>
    .white-background {
        background-color: white;
    }

    .username {
        margin-right: 15px;
    }
</style>
