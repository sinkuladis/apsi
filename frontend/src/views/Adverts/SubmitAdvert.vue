<template>
    <v-form ref="form" v-model="control.isFormValid">
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
                <v-row v-if="!isFree" class="justify-center">
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
                                v-model="control.imageFile"
                                outlined
                                show-size
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Dodaj zdjęcie główne"
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
                <v-row>
                    <v-col offset="9">
                        <v-btn
                                @click="submitAdvert"
                                :loading="loading"
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
        <v-overlay :value="overlay">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
    </v-form>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "SubmitAdvert",
        data() {
            return {
                loading: false,
                overlay: false,
                control: {
                    showPrice: '',
                    editAdvert: false,
                    isFormValid: false,
                    showSnackbar: false,
                    imageFile: null
                },

                text: {
                    snackbar: 'Wystąpił błąd!'
                },

                selectors: {
                    cities: [
                        'Warszawa', 'Wrocław', 'Toruń', 'Lublin',
                        'Zielona Góra', 'Łódź', 'Kraków',
                        'Opole', 'Rzeszów', 'Białystok', 'Gdańsk',
                        'Katowice', 'Kielce', 'Olsztyn', 'Poznań',
                        'Szczecin'
                    ],

                    categories: [
                        'Motoryzacja', 'Praca', 'Nieruchomości', 'Dom i Ogród',
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
                    title: '',
                    description: '',
                    price: 0,
                    for_free: false,
                    create_date: '',
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
                return this.control.showPrice === 'free'
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
                this.loading = true
                this.data.for_free = this.isFree
                if (this.data.for_free) {
                    this.data.price = 0
                }
                if (this.control.imageFile) {
                    await this.convertToBase64(this.control.imageFile)
                        .then((response) => {
                            this.data.image = response
                        }).catch(() => {
                            this.data.image = null
                        })
                }
                if (this.control.editAdvert) {
                    await this.axiosPatchAdvert()
                } else {
                    this.data.user = this.$store.getters.user.id
                    this.data.create_date = this.currentDate()
                    await this.axiosPostAdvert()
                }
            },
            currentDate: function () {
                function twoDigit(n) {
                    return (n < 10 ? '0' : '') + n;
                }

                const now = new Date();
                return '' + now.getFullYear() + '-'
                    + twoDigit(now.getMonth() + 1) + '-'
                    + twoDigit(now.getDate());
            },
            convertToBase64: (imageFile) => new Promise((resolve, reject) => {
                const reader = new FileReader()
                reader.onload = () => resolve(reader.result)
                reader.onerror = error => reject(error)
                reader.readAsDataURL(imageFile)
            }),
            axiosPatchAdvert: function() {
                axios({
                    method: 'PATCH',
                    url: `/api/adverts/${this.$route.params.id}/`,
                    data: this.data,
                    credentials: 'include',
                    headers: {'Authorization': 'Bearer ' + this.$store.getters.token}
                })
                    .then(() => {
                        this.$router.push(`/ad/${this.$route.params.id}`)
                    })
                    .catch(() => {
                        this.control.showSnackbar = true;
                    })
            },
            axiosPostAdvert: function() {
                axios({
                    method: 'POST',
                    url: '/api/adverts/',
                    data: this.data,
                    credentials: 'include',
                    headers: {'Authorization': 'Bearer ' + this.$store.getters.token}
                })
                    .then(() => {
                        this.$router.push(`/user/${this.$store.getters.user.id}/ads`)
                    })
                    .catch(() => {
                        this.control.showSnackbar = true;
                    })
            }
        },
        created: async function () {
            if (this.$route.name === "Edytowanie ogłoszenia") {
                this.overlay = true,
                this.control.editAdvert = true
                await axios({
                    method: 'GET',
                    url: `/api/adverts/${this.$route.params.id}/`,
                    credentials: 'include',
                    headers: {'Authorization': 'Bearer ' + this.$store.getters.token}
                })
                    .then((response) => {
                        this.data = {
                            advert_category: response.data.advert_category,
                            city: response.data.city,
                            promotion: response.data.promotion,
                            advert_status: response.data.advert_status,
                            title: response.data.title,
                            description: response.data.description,
                            price: response.data.price,
                            for_free: response.data.for_free,
                            create_date: response.data.create_date,
                        }
                    })
                    .catch(() => {
                        this.$router.push('/ad-not-found')
                    })
                this.overlay = false
            }
        }
    }
</script>

<style scoped>
</style>
