<template>
  <div class="main-body">
    <v-container style="width: 100%">
      <highlights-list
        column=true
        title="Ostatnio dodane"
        :items=ads
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
        error: false
      }
    },
    methods: {
      loadAdInfo: async function() {
        try {
          const resp = await this.$http.get(`/api/advertslatest/`);
          this.ads = resp.data;
          this.error = false
        } catch {
          this.error = true
        }
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