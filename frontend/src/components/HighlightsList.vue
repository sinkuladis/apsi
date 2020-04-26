<template>
    <div class="container">
        <h2>{{title}}</h2>
        <div class="inner-container">
            <md-card v-for="item in items" :key="item.message">
                <a href="#">
                    <img src="https://www.centrumrowerowe.pl/photo/product/rower-ns-bikes-eccentric-cromo-2-135709-f-sk6-w1550-h1080_2.png"/>
                    <span class="title">{{item.title}}</span>
                    <span class="price">{{item.price}}</span>
                </a>
            </md-card>
            <md-button class="md-raised">Zobacz więcej</md-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'HighlightsList',
        props: ['title', 'items']
    }
</script>

<style lang="scss" scoped>
    .container {
        flex-wrap: wrap;
        max-width: 100%;
        display: flex;
        vertical-align: top;
        border: 1px solid rgba(#000, .12);
        border-radius: 10px;
        padding: 15px;
        flex-direction: column;
        text-align: left;
        margin: 15px;

        h2 {
            margin: 0;
            margin-bottom: 10px;
        }

        .inner-container {
            display: flex;
            align-items: center;

            .md-card {
                border: 1px solid rgba(#000, .06);
                padding: 10px;
                border-radius: 4px;
                margin: 0 10px;
                width: 150px;

                    a {
                        display: flex;
                        flex-direction: column;
                        color: inherit;

                        .title {
                            color: darkslateblue;
                        }

                        .price {
                            font-size: 1.2em;
                        }

                        img {
                            width: 100px;
                            height: 100px;
                        }
                    }
            }

            .md-button {
                border-radius: 4px;
                background: #eee;
            }
        }
    }
</style>
