<template>
    <v-footer
            padless
            height="200"
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
                    <v-btn x-small text class="font-weight-light"><b-link href="/Help">pomoc</b-link></v-btn>
                    <v-btn @click="showPrivatePolicy()" x-small text class="font-weight-light">polityka prywatności</v-btn>
                    <v-btn :to="'/Rules'" x-small text class="font-weight-light">Regulamin</v-btn>
                    <v-btn @click="showCommercial()" x-small text class="font-weight-light">reklama</v-btn>
                    <v-btn @click="showAbout()" x-small text class="font-weight-light">jak działa</v-btn>
                    <v-btn @click="showCareer()" x-small text class="font-weight-light">kariera</v-btn>
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
        name: "BottomSection",
        methods: {
            showRules: function() {
                this.$router.push('/Rules')
            },
            showAbout: function() {
                this.$router.go('/About')
            },
            showCareer: function() {
                this.$router.push('/Career')
            },
            showCommercial: function() {
                this.$router.push('/Commercial')
            },
            showHelp: function() {
                this.$router.push('/Help')
            },
            showPrivatePolicy: function() {
                this.$router.push({ path: '/' })
                this.$router.push({ name: 'PrivatePolicy'})
            }
        }
    }
</script>

<style scoped>

</style>
