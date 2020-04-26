<template>
    <div class="container">
        <p class="display-3 font-italic font-weight-thin">Categories Picker</p>
    </div>
</template>

<script>
    export default {
        name: 'CategoriesPicker',
        data: () => {
            return { items: [{message: 'test1'}, {message: 'test2'}, {message: 'test3'}]}
        }
    }
</script>

<style lang="scss" scoped>
    .container {
        flex-wrap: wrap;
        width: 320px;
        max-width: 100%;
        display: inline-block;
        vertical-align: top;
    }
</style>
