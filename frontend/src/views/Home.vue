<template>
    <div class="main-body">
        <categories-picker/>
        <highlights-list/>
    </div>
</template>

<script>
    import CategoriesPicker from "@/components/CategoriesPicker";
    import HighlightsList from "@/components/HighlightsList";
    export default {
        name: 'Home',
        components: {HighlightsList, CategoriesPicker}
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