<template>
    <div>
        <!--Grey area section-->
        <section class="grey lighten-4 text-center">
            <search-section />
            <categories-picker/>
        </section>

        <!--White area section-->
        <highlights-list/>
    </div>
</template>

<script>
    import CategoriesPicker from "@/components/CategoriesPicker";
    import HighlightsList from "@/components/HighlightsList";
    import SearchSection from "@/components/SearchSection";

    export default {
        name: 'Home',
        components: {HighlightsList, CategoriesPicker, SearchSection}
    }
</script>

<style scoped>
    /*.content {*/
    /*    display: flex;*/
    /*    flex-direction: column;*/
    /*    justify-content: center;*/
    /*    align-items: center;*/
    /*}*/
</style>
