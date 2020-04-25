<template>
    <div class="main-body">
        <search-section />
        <categories-picker class="content"/>
        <highlights-list class="content"/>
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
    .content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>
