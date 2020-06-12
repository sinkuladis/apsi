<template>
    <div class="container">
        <div class="categories-container">
            <md-button 
                class="md-raised md-primary category"
                v-for="category in categories" :key="category.message"
                @click="onCategoryClick(category.name)"
            >
                <span><v-icon large>{{category.icon}}</v-icon></span>
                <span>{{category.name}}</span>
            </md-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'CategoriesPicker',
        props: ['categories', 'onCategoryClick']
    }
</script>

<style lang="scss" scoped>
    .container {
        flex-wrap: wrap;
        display: inline-block;
        vertical-align: top;

        .categories-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            width: 80%;
            margin: auto;

            .category {
                width: 130px;
                height: 65px;
                border-radius: 4px;
                margin: 5px;
            }

            .category span {
                display: block;
            }
        }
    }
</style>
