<template>
  <div class="main-body">
    <div class="header">
      <span><strong>Kategoria:</strong>{{ad.advert_category}}</span>
      <span><strong>Zamieszczone:</strong> {{ad.create_date}}</span>
    </div>
    <v-row>
      <v-col cols="6">
        <img v-bind:src="ad.image"/> 
      </v-col> 
      <v-col cols="6" class="details">
        <h1 class="ad-title">{{ad.title}}</h1>
        <p class="price">{{ad.for_free ? "Darmowy" : ad.price + "zł"}}</p>
        <p class="seller"><strong>Wystawiający:</strong> <a @click="redirectToSeller(ad.user.id)">{{ad.user.username}}</a></p>
        <p class="city"><strong>Lokalizacja:</strong> {{ad.city}}</p>
      </v-col> 
    </v-row>      
    <p class="description">{{ad.description}}</p>
  </div>
</template>

<script>
  

  export default {
    data() {
      return {
        ad: {
          "title": "Rower",
          "image": "",
          "description": "PEGASUS ALU COMFORT MILLENNIUM MADE IN GERMANY \
                          Rower w stanie bardzo dobrym, zdjęcia realne \
                          Amortyzowana solidna rama aluminiowa \
                          Z przodu amortyzator SR SUNTOUR T810 (stan techniczny bardzo dobry) \
                          cały na osprzęcie Shimano \
                          Koła 28- aluminiowe czarne stożkowe, podwójnie wzmacniane felgi- GERMENY ALLOY ALL TERRAIN RIM SYSTEM \
                          Aluminiowe piasty \
                          Nowe opony Continental Contact II Reflex 28 x 1.6 \
                          Więcej informacji pod telefonem",
          "price": 100,
          "for_free": false,
          "advert_category": "",
          "city": "",
          "create_date": "2020-05-21",
          "user": "",
          "promotion_id": 0,
          "advert_status_id": 0
        }
      }
    },
    methods: {
      loadAdInfo: async function() {
        try {
          const resp = await this.$http.get(`/api/adverts/${this.$route.params.id}/`);
          this.ad = resp.data;
        } catch {
          this.$router.replace('/ad-not-found')
        }
      },
      redirectToSeller: function(id) {
          this.$router.push(`/user/${id}/ads`)
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
      width: 80%;
      margin: auto;
      padding-bottom: 10rem;

      img {
        width: 300px;
        height: 240px;
      }
  }

  .details {
    align-items: center;
    justify-content: center;
    display: flex;
    flex-direction: column;
  }

  .ad-title {
    font-size: 2.5rem;
    text-align: center;
  }

  .price {
    margin: 0 auto;
    color: #666;
  }

  .description {
    margin: 20px;
    text-align: justify;
  }

  .city {
    font-size: 1rem;
    color: #666;
    margin: 0;
    text-align: center;
  }

  .header {
    margin: 10px;
    width: 95%;
    display: flex;
    justify-content: space-between;

    span {
      font-size: 1.1rem;
      align-self: flex-start;
    }
  }

  .seller {
    font-size: 1rem;
    color: #666;
    margin: 0;
    text-align: center;
    margin: 10px;
  }
</style>