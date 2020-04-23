<template>
    <v-footer
            dark
            padless
            absolute
    >
        <v-card
                flat
                tile
                class="indigo lighten-1 white--text text-center">
            <v-card-text class="white--text">
                <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat nemo hic corporis, voluptates rerum quo quisquam vitae eos ipsum neque tenetur excepturi consectetur optio, dolores fugiat totam repellendus! Dolor, similique.
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat nemo hic corporis, voluptates rerum quo quisquam vitae eos ipsum neque tenetur excepturi consectetur optio, dolores fugiat totam repellendus! Dolor, similique.
                </p>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-text class="white--text">
                {{ new Date().getFullYear() }} —
                    <span class="font-weight-light">Olx</span>
                    <span class="font-weight-medium">ample</span>
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
    export default {
        name: "BottomSection"
    }
</script>

<style scoped>

</style>
