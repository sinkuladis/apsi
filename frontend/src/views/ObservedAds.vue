<template>
  <div class="main-body">
    <highlights-list 
        title="Obserwowane"
        column=true
        :items=ads
    />
  </div>
</template>

<script>
 // 
  import HighlightsList from "@/components/HighlightsList";

  export default {
    components: { HighlightsList },
    data() {
      return {
        ads: [
          { title: 'Obserwowany 1', price: "3zł", id: '0'}, 
          { title: 'Obserwowany 2', price: "300zł", id: '0'}, 
          { title: 'Obserwowany 3', price: "123zł", id: '0'}
        ],
        error: false
      }
    },
    methods: {
      loadAdInfo: async function() {
        try {
           //to be changed once backend ready
          // const resp = await this.$http.get(`http://localhost:8080/api/adverts/${this.$route.params.id}/`);
          // this.ads = resp.data;
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
</style>