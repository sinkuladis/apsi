<template>
  <div class="main-body">
    <p 
      v-if="ads.length === 0"
      class="observed-info"
    >
      Jeszcze niczego nie obserwujesz.
    </p>
    <highlights-list 
      v-else
      title="Obserwowane"
      column=true
      :items=ads
    />
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
          const resp = await this.$http.get(`http://localhost:8080/api/adverts/${this.$route.params.id}/`);
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
</style>