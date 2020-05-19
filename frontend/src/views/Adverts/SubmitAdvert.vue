<template>
        <v-form ref="form" v-model="valid">
            <v-container class="text-center">

                <!--Tytuł i kategorie-->
                <v-card class="my-3">
                    <v-row class="title font-weight-light justify-center">
                        <v-col cols="4" class="pb-0 ">
                            Wpisz tytuł
                        </v-col>
                        <v-col cols="4" class="pb-0">
                            Wybierz kategorię
                        </v-col>
                    </v-row>
                    <v-row class="justify-center">
                        <v-col cols="4" class="ms-6">
                            <v-text-field
                                    :rules="requiredRule"
                                    placeholder="Tytuł"
                                    outlined
                            ></v-text-field>
                        </v-col>
                        <v-col cols="4" class="ms-6">
                            <v-select
                                    :rules="requiredRule"
                                    :items="items"
                                    outlined
                                    placeholder="Kategoria"
                            ></v-select>
                        </v-col>
                    </v-row>
                </v-card>

                <!--Cena-->
                <v-card class="my-3">
                    <v-row class="justify-center">
                        <v-col cols="4">
                            <v-btn-toggle
                                    v-model="price"
                                    tile
                                    group
                                    color="blue"
                                    mandatory>
                                <v-btn value="value">Cena</v-btn>
                                <v-btn value="free">Za darmo</v-btn>
                            </v-btn-toggle>
                        </v-col>
                    </v-row>
                    <v-row v-if="price === 'value'" class="justify-center">
                        <v-col cols="4" class="ms-6">
                            <v-text-field
                                    :rules="requiredRule"
                                    outlined
                                    placeholder="Cena"
                                    suffix="zł"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card>

                <!--Opis-->
                <v-card class="my-3">
                    <v-row class="title font-weight-light justify-center">
                        <v-col cols="4" class="pb-0 ps-0">
                            Dodaj opis
                        </v-col>
                    </v-row>
                    <v-row class="justify-center">
                        <v-col cols="8" class="ms-6">
                            <v-textarea
                                    :rules="requiredRule"
                                    outlined
                                    name="input-7-4"
                                    placeholder="Opis"
                            ></v-textarea>
                        </v-col>
                    </v-row>
                </v-card>

                <!--Zdjęcia-->
                <v-card class="my-3">
                    <v-row class="title font-weight-light justify-center">
                        <v-col cols="4" class="pb-0 ms-1">
                            Dodaj zdjęcia
                        </v-col>
                    </v-row>

                    <v-row class="justify-center">
                        <v-col cols="5" class="ms-6">
                            <v-file-input
                                    outlined
                                    accept="image/png, image/jpeg, image/bmp"
                                    placeholder="Dodaj zdjęcie główne"
                                    prepend-inner-icon="mdi-camera"
                                    prepend-icon=""
                            ></v-file-input>
                        </v-col>
                    </v-row>
                    <v-row class="justify-center">
                        <v-col cols="3" class="ms-6">
                            <v-file-input
                                    outlined
                                    accept="image/png, image/jpeg, image/bmp"
                                    placeholder="Dodaj zdjęcie"
                                    prepend-inner-icon="mdi-camera"
                                    prepend-icon=""
                            ></v-file-input>
                        </v-col>
                        <v-col cols="3">
                            <v-file-input
                                    outlined
                                    accept="image/png, image/jpeg, image/bmp"
                                    placeholder="Dodaj zdjęcie"
                                    prepend-inner-icon="mdi-camera"
                                    prepend-icon=""
                            ></v-file-input>
                        </v-col>
                        <v-col cols="3">
                            <v-file-input
                                    outlined
                                    accept="image/png, image/jpeg, image/bmp"
                                    placeholder="Dodaj zdjęcie"
                                    prepend-inner-icon="mdi-camera"
                                    prepend-icon=""
                            ></v-file-input>
                        </v-col>
                    </v-row>
                </v-card>

                <!--Dane kontaktowe-->
                <v-card class="my-3">
                    <v-row>
                        <v-col>
                            <span class="title font-weight-light">Twoj dane kontaktowe</span>
                        </v-col>
                    </v-row>
                    <v-row justify="center">
                        <v-col cols="6" class="ms-6">
                            <v-text-field
                                    :rules="requiredRule"
                                    label="Podaj lokalizację"
                                    outlined
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row justify="center">
                        <v-col cols="6" class="ms-6">
                            <v-text-field
                                    v-model="name"
                                    :rules="requiredRule"
                                    label="Podaj imię"
                                    outlined
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row justify="center">
                        <v-col cols="6" class="ms-6">
                            <v-text-field
                                    v-model="email"
                                    :rules="emailRules"
                                    label="Adres e-mail"
                                    outlined
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card>

                <!--Submit button-->
                <v-card>
                    <v-row>
                        <v-col offset="9">
                            <v-btn
                                    @click="validate"
                                    depressed
                                    dark
                                    color="orange">
                                Zatwierdź
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card>


            </v-container>
        </v-form>
</template>

<script>
    const axios = require('axios');

    export default {
        name: "SubmitAdvert",
        data() {
            return {
                valid: false,
                name: '',
                email: '',
                price: 'value',

                apiData: null,
                error: false,

                // Rules definition
                emailRules: [
                    v => !!v || 'Proszę podać adres poczty elekronicznej',
                    v => /.+@.+/.test(v) || 'Adres nie jest poprawny',
                ],
                requiredRule: [
                    v => !!v || 'To pole jest wymagane'
                ],
            }
        },
        methods: {
            validate() {
                this.$refs.form.validate()
            },
        }
    }
</script>

<style scoped>
</style>
