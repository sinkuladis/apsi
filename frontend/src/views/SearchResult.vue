<template>
    <v-card>
        <v-data-table
                :headers="headers"
                :items="adverts"
                @click:row="viewAdvert"
                class="elevation-1 search"
        >
            <template v-slot:item.image="{ item }">
                <v-img :src="item.image" height="100" widht="100"></v-img>
            </template>

            <template v-slot:item.price="{ item }">
                <span>{{item.for_free ? "Darmowy" : item.price}}</span>
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
    .search {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 80%;
        margin: auto;
        padding-bottom: 2rem;
    }
</style>
