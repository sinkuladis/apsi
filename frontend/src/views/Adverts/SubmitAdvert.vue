<template>
    <v-form ref="form" v-model="control.isFromValid">
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
                                :rules="rules.required"
                                placeholder="Tytuł"
                                outlined
                                v-model="data.title"
                        ></v-text-field>
                    </v-col>
                    <v-col cols="4" class="ms-6">
                        <v-select
                                :rules="rules.required"
                                :items="selectors.categories"
                                v-model="data.advert_category"
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
                                v-model="control.showPrice"
                                tile
                                group
                                color="blue"
                                mandatory>
                            <v-btn value="value">Cena</v-btn>
                            <v-btn value="free">Za darmo</v-btn>
                        </v-btn-toggle>
                    </v-col>
                </v-row>
                <v-row v-if="isFree" class="justify-center">
                    <v-col cols="4" class="ms-6">
                        <v-text-field
                                :rules="rules.required"
                                outlined
                                v-model="data.price"
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
                                :rules="rules.required"
                                outlined
                                name="input-7-4"
                                placeholder="Opis"
                                v-model="data.description"
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
                        <v-select
                                :rules="rules.required"
                                :items="selectors.cities"
                                v-model="data.city"
                                outlined
                                placeholder="Miasto"
                        ></v-select>
                    </v-col>
                </v-row>
            </v-card>

            <!--Submit button-->
            <v-card>
                <div>{{control.editAdvert}}</div>
                <v-row>
                    <v-col offset="9">
                        <v-btn
                                @click="submitAdvert"
                                depressed
                                dark
                                color="orange">
                            Zatwierdź
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card>
        </v-container>
        <v-snackbar v-model="control.showSnackbar" :timeout="2000">
            {{ text.snackbar }}
            <v-btn
                    color="blue"
                    text
                    @click="snackbar = false"
            >
                Close
            </v-btn>
        </v-snackbar>
    </v-form>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "SubmitAdvert",
        data() {
            return {
                control: {
                    showPrice: '',
                    editAdvert: false,
                    isFromValid: false,
                    showSnackbar: false,
                },

                text: {
                    snackbar: "Wystąpił błąd!"
                },

                selectors: {
                    cities: [
                        'Warszawa', 'Wrocław', 'Toruń', 'Lublin',
                        'Zielona Góra', 'Łódź', 'Kraków', 'Warszawa',
                        'Opole', 'Rzeszów', 'Białystok', 'Gdańsk',
                        'Katowice', 'Kielce', 'Olsztyn', 'Poznań',
                        'Szczecin'
                    ],

                    categories: [
                        'Motoryzacja', 'Praca', 'Nieruchomość', 'Dom i ogród',
                        'Elektronika', 'Moda', 'Rolnictwo', 'Zwierzęta', 'Dla Dzieci',
                        'Sport i Hobby', 'Muzyka i Edukacja', 'Usługi i Firmy',
                        'Ślub i Wesele', 'Oddam za darmo', 'Zamienię', 'Dla ogrodu'
                    ],
                },

                data: {
                    advert_category: '',
                    city: '',
                    promotion: 'Zwykły',
                    advert_status: 'Aktywne',
                    user: '',
                    title: '',
                    description: '',
                    price: 0.01,
                    for_free: this.isFree,
                    create_date: ''
                },

                rules: {
                    email: [
                        v => !!v || 'Proszę podać adres poczty elekronicznej',
                        v => /.+@.+/.test(v) || 'Adres nie jest poprawny',
                    ],
                    required: [
                        v => !!v || 'Pole jest wymagane'
                    ],
                }
            }
        },
        computed: {
            isFree: function () {
                return this.control.showPrice === 'value'
            },
            price: function () {
                return this.isFree ? 0 : this.data.price
            }
        },
        methods: {
            validate: function () {
                this.$refs.form.validate()
            },
            submitAdvert: async function () {
                if (!this.$refs.form.validate()) {
                    return
                }
                this.data.for_free = this.isFree
                if (this.control.editAdvert){
                    console.log('PUT')
                    console.log(this.data)
                    await axios.put(`/api/adverts/${this.$route.params.id}/`, this.data)
                        .then(() => {
                            this.$router.push('/')
                        })
                        .catch(() => {
                            this.control.showSnackbar = true;
                        })
                } else {
                    this.data.user = this.$store.getters.user.username
                    this.data.create_date = this.currentDate()
                    await axios.post('/api/adverts/', this.data)
                        .then(() => {
                            this.$router.push('/')
                        })
                        .catch(() => {
                            this.control.showSnackbar = true;
                        })
                }
            },
            currentDate: function () {
                function twoDigit(n) {
                    return (n < 10 ? '0' : '') + n;
                }

                var now = new Date();
                return '' + now.getFullYear() + '-'
                    + twoDigit(now.getMonth() + 1) + '-'
                    + twoDigit(now.getDate());
            }
        },
        created: async function () {
            if (this.$route.name === "Edytowanie ogłoszenia") {
                this.control.editAdvert = true
                await axios.get(`/api/adverts/${this.$route.params.id}/`)
                    .then((response) => {
                        this.data = {
                                advert_category: response.data.advert_category,
                                city: response.data.city,
                                promotion: response.data.promotion,
                                advert_status: response.data.advert_status,
                                user: response.data.user,
                                title: response.data.title,
                                description: response.data.description,
                                price: response.data.price,
                                for_free: response.data.for_free,
                                create_date: response.data.create_date
                        }
                    })
                    .catch(() => {
                        this.$router.push('/ad-not-found')
                    })
            }
        }
    }
</script>

<style scoped>
</style>
