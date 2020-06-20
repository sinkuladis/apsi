<template>
    <v-card>
        <v-data-table
                :headers="headers"
                :items="adverts"
                @click:row="viewAdvert"
                class="elevation-1"
        >
            <template v-slot:item.image>
                <v-img src="https://picsum.photos/100" height="100" widht="100"></v-img>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
    export default {
        name: "SearchResult",
        data() {
            return {
                headers: [
                    {text: '', align: 'start', sortable: false, value: 'image'},
                    {text: 'Tytuł', value: 'title'},
                    {text: 'Miasto', value: 'city'},
                    {text: 'Kategoria', value: 'advert_category'},
                    {text: 'Cena', value: 'price'}
                ],
                adverts: []
            }
        },
        methods: {
            loadSearchResult: function () {
                this.adverts = this.$store.getters.adverts
            },
            viewAdvert: function(advert) {
                this.$router.push(`/ad/${advert.id}`)
            }
        },
        created() {
            this.loadSearchResult()
        }
    }
</script>

<style scoped>

</style>
