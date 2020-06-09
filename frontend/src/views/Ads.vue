<template>
  <div class="main-body">
    <p 
      v-if="ads.length === 0"
      class="observed-info"
    >
      Jeszcze nie umieściłeś ogłoszenia.
    </p>
    <v-container v-else style="width: 100%">
      <div class="options">
        <v-btn @click="changeSelection('Aktywne')">Aktywne</v-btn>
        <v-btn @click="changeSelection('Zakończone')">Zakończone</v-btn>
        <v-btn @click="changeSelection('Oczekujące')">Oczekujące</v-btn>
      </div>
      <highlights-list
        column=true
        :title=selectedType
        :items=shownAds
      />
    </v-container>
  </div>
</template>

<script>
  import HighlightsList from "@/components/HighlightsList";

  export default {
    components: { HighlightsList },
    data() {
      return {
        ads: [],
        shownAds: [],
        error: false,
        selectedType: "Aktywne"
      }
    },
    methods: {
      loadAdInfo: async function() {
        try {
          const resp = await this.$http.get(`/api/adverts/${this.$route.params.id}/`);
          this.ads = resp.data;
          this.changeSelection(this.selectedType)
          this.error = false
        } catch {
          this.error = true
        }
      },
      changeSelection: function(type) {
          this.selectedType = type
          this.shownAds = this.ads.filter(ad => ad.type === type)
      }
    },
    created() {
      this.loadAdInfo();
    }
  }
</script>

<style scoped lang="scss">
    .main-body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-bottom: 10rem;
    }

    .observed-info {
      margin: 40px;
      font-size: 1.5rem;
    }
    
    .options {
      display: flex;
      justify-content: center;

      button {
        margin: 5px;
      }
    }
</style>