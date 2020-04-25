<template>
    <v-footer
            padless
            absolute
            class="white">
        <v-container class="py-0">
            <v-card
                    flat
                    tile
                    class="text-center font-weight-thin">
                <v-divider></v-divider>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt magni quis natus molestias ducimus ex deleniti laboriosam, quaerat dolorum maiores pariatur error voluptatem esse molestiae repellat dolore exercitationem? Velit, molestiae.</p>
                <v-divider></v-divider>
                <v-container>
                    <v-btn x-small text class="font-weight-light">pomoc</v-btn>
                    <v-btn x-small text class="font-weight-light">polityka prywatności</v-btn>
                    <v-btn x-small text class="font-weight-light">Regulamin</v-btn>
                    <v-btn x-small text class="font-weight-light">reklama</v-btn>
                    <v-btn x-small text class="font-weight-light">jak działa</v-btn>
                    <v-btn x-small text class="font-weight-light">kariera</v-btn>
                </v-container>
                <v-divider></v-divider>
                <v-card-text class="py-2">
                    {{ new Date().getFullYear() }} —
                    <span class="font-weight-light">Olx</span>
                    <span class="font-weight-medium">ample</span>
                </v-card-text>
            </v-card>
        </v-container>
    </v-footer>
</template>

<script>
    export default {
        name: "BottomSection"
    }
</script>

<style scoped>

</style>
