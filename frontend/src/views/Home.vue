<template>
    <div class="main-body">
        <!--Grey area section-->
        <section class="grey lighten-4 text-center width-100">
            <search-section />
            <categories-picker
                :categories=categories
                :onCategoryClick=loadAdsByCategory
            />
        </section>
        <section v-if="lastAdded.length !== 0">
            <!--White area section-->
            <highlights-list
                title="Ostatnio dodane"
                :items=lastAdded
                :onClick="showMoreLastAdded"
            />
        </section>
    </div>
</template>

<script>
    import CategoriesPicker from "@/components/CategoriesPicker";
    import HighlightsList from "@/components/HighlightsList";
    import SearchSection from "@/components/SearchSection";
    export default {
        name: 'Home',
        components: { HighlightsList, CategoriesPicker, SearchSection},
        data: () => {
            return {
                    lastAdded: [],
                    categories: [
                        { icon: 'mdi-car', name: 'Motoryzacja' },
                        { icon: 'mdi-home', name: 'Nieruchomości' },
                        { icon: 'mdi-worker', name: 'Praca' },
                        { icon: 'mdi-sofa', name: 'Dom i ogród' },
                        { icon: 'mdi-laptop', name: 'Elektronika' },
                        { icon: 'mdi-tshirt-crew', name: 'Moda' },
                        { icon: 'mdi-dog-side', name: 'Zwierzęta' },
                        { icon: 'mdi-human-child', name: 'Dla dzieci' },
                        { icon: 'mdi-basketball', name: 'Sport' },
                        { icon: 'mdi-book-open', name: 'Edukacja' },
                        { icon: 'mdi-guitar-acoustic', name: 'Muzyka' },
                        { icon: 'mdi-postage-stamp', name: 'Hobby' }
                    ],
                    isSearched: false,
                    searchedAds: []
                }
        },
        created() {
            this.loadLastAdded();
        },
        methods: {
            loadAdsByCategory: async function(categoryName) {
                    try {
                        const resp = await this.$http.get(`/api/adverts/`, { params: { advert_category__name: categoryName } });
                        this.searchedAds = resp.data;
                        this.$store.commit('storeSearch', resp.data)
                        this.isSearched = true
                        this.$router.push('/search')
                    } catch {
                       console.log("kek") 
                    }
                },
            loadLastAdded: async function() {
                try {
                    const resp = await this.$http.get(`/api/advertslatest/`);
                    this.lastAdded = resp.data.slice(0,3)
                    this.error = false
                } catch {
                    this.error = true
                }
            },
            showMoreLastAdded: function() {
                this.$router.push(`/latest`)
            }
        }
    }
</script>

<style scoped>
    .main-body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-bottom: 10rem;
    }

    .width-100 {
        width: 100%;
    }
</style>
