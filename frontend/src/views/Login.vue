<template>
    <v-container class="my-15">
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
                                        <v-text-field dense outlined label="E-mail">
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
                                                @click:append="showPass = !showPass">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-btn :ripple="false" block depressed dark color="light-blue">Załoguj się</v-btn>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-tab-item>

                        <v-tab href="#signup">Rejestracja</v-tab>
                        <v-tab-item value="signup">
                            <v-container>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field dense outlined label="E-mail">
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
                                                @click:append="showPass = !showPass">
                                        </v-text-field>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col>
                                        <v-checkbox
                                                class="font-weight-light ma-0 pa-0"
                                                v-model="checkbox"
                                                :label="`Wyrażam zgodę`"
                                        ></v-checkbox>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col cols="12">
                                        <v-btn :ripple="false" block depressed dark color="light-blue">Zarejestruj się</v-btn>
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
    export default {
        name: "Login",
        data() {
            return {
                showPass: false,
                checkbox: false
            }
        }
    }
</script>

<style scoped>
</style>
