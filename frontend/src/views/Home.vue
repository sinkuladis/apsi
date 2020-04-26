<template>
    <div class="main-body">
        <categories-picker/>
        <highlights-list 
            title="Ogłoszenia promowane"
            :items=promotedItems
        />
        <highlights-list 
            title="Ostatnio dodane"
            :items=lastAdded
        />
    </div>
</template>

<script>
    import CategoriesPicker from "@/components/CategoriesPicker";
    import HighlightsList from "@/components/HighlightsList";
    export default {
        name: 'Home',
        components: { HighlightsList, CategoriesPicker },
        data: () => {
            return { 
                    promotedItems: [
                        { title: 'Promowany 1', price: "3zł"}, 
                        { title: 'Promowany 2', price: "300zł"}, 
                        { title: 'Promowany 3', price: "123zł"}
                    ],
                    lastAdded: [
                        { title: 'Ostatnio dodany 1', price: "54zł"}, 
                        { title: 'Ostatnio dodany 2', price: "124zł"}, 
                        { title: 'Ostatnio dodany 3', price: "500zł"}
                    ],
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
    }
</style>