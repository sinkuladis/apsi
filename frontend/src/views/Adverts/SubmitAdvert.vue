<template>
    <div>
        <v-container class="text-center">

            <!--Tytuł i kategorie-->
            <v-card class="my-3">
                <v-row class="subtitle-1 font-weight-regular">
                    <v-col cols="4" class="pb-0">
                        Wpisz tytuł
                    </v-col>
                    <v-col cols="4" class="pb-0 ms-5">
                        Wybierz kategorię
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" class="ms-6">
                        <v-text-field
                                placeholder="Tytuł"
                                filled
                        ></v-text-field>
                    </v-col>
                    <v-col cols="4" class="ms-6">
                        <v-select
                                :items="items"
                                filled
                                placeholder="Filled style"
                        ></v-select>
                    </v-col>
                </v-row>
            </v-card>

            <!--Opis-->
            <v-card class="my-3">
                <v-row class="subtitle-1 font-weight-regular">
                    <v-col cols="4" class="pb-0 ps-0">
                        Dodaj opis
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="6" class="ms-6">
                        <v-textarea
                                filled
                                name="input-7-4"
                                label="Opis"
                        ></v-textarea>
                    </v-col>
                </v-row>
            </v-card>

            <!--Zdjęcia-->
            <v-card class="my-3">
                <v-row class="subtitle-1 font-weight-regular">
                    <v-col cols="4" class="pb-0 ms-1">
                        Dodaj zdjęcia
                    </v-col>
                </v-row>

                <v-row>
                    <v-col cols="5" class="ms-6">
                        <v-file-input
                                :rules="rules"
                                filled
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Dodaj zdjęcie główne"
                                prepend-icon="mdi-camera"
                        ></v-file-input>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="3" class="ms-6">
                        <v-file-input
                                filled
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Dodaj zdjęcie"
                        ></v-file-input>
                    </v-col>
                    <v-col cols="3">
                        <v-file-input
                                filled
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Dodaj zdjęcie"
                        ></v-file-input>
                    </v-col>
                    <v-col cols="3">
                        <v-file-input
                                filled
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Dodaj zdjęcie"
                        ></v-file-input>
                    </v-col>
                </v-row>
            </v-card>

            <!--Dane kontaktowe-->
            <v-card class="my-3">
                <v-row class="subtitle-1 font-weight-regular">
                    <v-col cols="4" class="pb-0 ps-0 ms-8">
                        Podaj lokalizację
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" class="ms-6">
                        <v-text-field
                                placeholder="Lokalizacja"
                                filled
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="subtitle-1 font-weight-regular">
                    <v-col cols="4" class="pb-0 ps-0 ms-8">
                        Podaj swoje imię
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" class="ms-6">
                        <v-text-field
                                placeholder="Imię"
                                filled
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="subtitle-1 font-weight-regular">
                    <v-col cols="4" class="pb-0 ps-0 ms-8">
                        Podaj adres e-mail
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4" class="ms-6">
                        <v-text-field
                                placeholder="Adres e-mail"
                                filled
                        ></v-text-field>
                    </v-col>
                </v-row>
            </v-card>
            <v-card>
                <v-row>
                    <v-col offset="10">
                        <v-btn depressed dark color="orange">
                            Zatwierdź
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card>
        </v-container>
    </div>
</template>

<script>
    export default {
        name: "SubmitAdvert"
    }
</script>

<style scoped>
</style>
