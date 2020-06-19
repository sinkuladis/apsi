<template>
    <div v-bind:class="getListClass">
        <h2>{{title}}</h2>
        <div class="inner-container">
            <md-card v-for="item in items" :key="item.message">
                <a v-on:click="redirectTo(item.id)">
                    <img v-bind:src="item.image"/> 
                    <v-col class="inner">
                        <span class="title">{{item.title}}</span>
                        <span>{{item.advert_category}}</span>
                    </v-col>
                    <span class="price">{{item.price}}zł</span>
                </a>
            </md-card>
            <md-button v-if="!column" class="md-raised" @click="onClick">Zobacz więcej</md-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'HighlightsList',
        props: ['title', 'items', 'column', 'onClick'],
        methods: {
            redirectTo: function(id) {
                this.$router.push(`/ad/${id}`)
            }
        },
        computed: {
            getListClass: function() {
                return this.column ? 'container type-column' : 'container';
            }
        }
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
        margin: 15px 0;

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
                        cursor: pointer;

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

    .type-column {
        h2 {
            text-align: center;
            font-size: 2rem;
        }
        .inner-container {
            flex-direction: column;

            .md-card {
                width: 50%;
                padding: 10px 20px;
                a {
                    flex-direction: row;
                    justify-content: space-between;
                    align-items: center;
                }
            }
        }
    }

    .inner {
        display: flex;
        flex-direction: column;
    }
</style>
