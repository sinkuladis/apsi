<template>
    <v-container class="my-15 fixed-width">
        <v-row justify="center">
            <v-col cols="7">
                <v-card elevation="24">
                    <v-tabs color="blue" fixed-tabs>
                        <v-tabs-slider color="blue"></v-tabs-slider>
                        <v-tab href="#login">Logowanie</v-tab>
                        <v-tab-item value="login">
                            <v-container>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field dense outlined v-model="loginData.username" label="Username">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field
                                                dense
                                                outlined
                                                flat
                                                label="Hasło"
                                                :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
                                                :type="showPass ? 'text' : 'password'"
                                                counter
                                                v-model="loginData.password"
                                                @click:append="showPass = !showPass">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-btn 
                                            :ripple="false" 
                                            block 
                                            depressed 
                                            v-on:click="login" 
                                            dark color="light-blue">Zaloguj się</v-btn>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-tab-item>
                    
                        <v-tab href="#signup">Rejestracja</v-tab>
                        <v-tab-item value="signup">
                            <v-container>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field dense v-model="registrationData.username" outlined label="Username">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field dense v-model="registrationData.email" outlined label="E-mail">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field dense v-model="registrationData.firstName" outlined label="Imię">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field dense v-model="registrationData.lastName" outlined label="Nazwisko">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field
                                                dense
                                                outlined
                                                flat
                                                label="Hasło"
                                                :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
                                                :type="showPass ? 'text' : 'password'"
                                                counter
                                                 v-model="registrationData.password"
                                                @click:append="showPass = !showPass">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col>
                                        <v-checkbox
                                                class="font-weight-light ma-0 pa-0"
                                                v-model="checkbox"
                                                :label="`Wyrażam zgodę na rejestrację.`"
                                        ></v-checkbox>
                                    </v-col>
                                </v-row>
                                <v-row v-if="registerError">
                                    <v-col>
                                        <p class="error">
                                            Wystąpił błąd. Spróbuj ponownie.
                                        </p>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-btn  :ripple="false" 
                                                block 
                                                depressed 
                                                dark 
                                                color="light-blue"
                                                v-on:click="register">Zarejestruj się</v-btn>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-tab-item>
                    </v-tabs>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import axios from 'axios'
    import Vue from 'vue'

    export default {
        name: "Login",
        data() {
            return {
                loginData: {
                    username: '',
                    password: ''
                },
                registrationData: {
                    username: '',
                    email: '',
                    firstName: '',
                    lastName: '',
                    password: ''
                },
                registerValidationErrors: {},
                registerError: false,
                showPass: false,
                checkbox: false
            }
        },
        methods: {
            register: async function () {
                const data = this.registrationData;
                try {
                    const resp = await axios.post("http://localhost:8080/api/users/", 
                        {
                            "username": data.username,
                            "last_name": data.lastName,
                            "first_name": data.firstName,
                            "email": data.email,
                            "password": data.password
                        },
                        {
                            mode: 'cors', 
                            credentials: 'same-origin', 
                            headers: {
                                'Content-Type': 'application/json'
                            },
                        }
                    );
                    if (resp.status === 201){
                        this.registerError = false;
                        this.registerValidationErrors = {};
                        this.login({
                            username: data.username, 
                            password: data.password
                        });
                    }
                } catch (e) {
                    this.registerValidationErrors = e.response;
                    this.registerError = true;
                }
            },
            login: async function ({username, password}) {
                try {
                    const resp = await axios.post("http://localhost:8080/api/token/", 
                        {
                            "username": username ?? this.loginData.username,
                            "password": password ?? this.loginData.password
                        },
                        {
                            mode: 'cors', 
                            credentials: 'same-origin', 
                            headers: {
                                'Content-Type': 'application/json'
                            },
                        }
                    );
                    if (resp.status === 200){
                        Vue.prototype.loggedIn = true;
                    } 
                } catch (e) {
                    console.log(e)
                }
            }
        }
    }
</script>

<style scoped>
    .fixed-width {
        width: 700px;
        padding-bottom: 10rem;
    }
</style>
