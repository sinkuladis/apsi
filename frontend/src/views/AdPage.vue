<template>
  <div class="main-body">
    <div class="header">
      <span><strong>Kategoria:</strong> Dom i ogród</span>
      <span><strong>Zamieszczone:</strong> {{ad.create_date}}</span>
    </div>
    <img src="https://www.centrumrowerowe.pl/photo/product/rower-ns-bikes-eccentric-cromo-2-135709-f-sk6-w1550-h1080_2.png"/>       
    <h1 class="ad-title">{{ad.title}} <span>{{ad.for_free ? "Darmowy" : ad.price + "zł"}}</span></h1>
    <span class="city">Warszawa</span>
    <span class="seller"><strong>Wystawiający:</strong> <a>{{ad.user_id}}</a></span>
    <p class="description">{{ad.description}}</p>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        ad: {
          "title": "Rower",
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
          "advert_category_id": 0,
          "city_id": 0,
          "create_date": "2020-05-21",
          "user_id": "1235142",
          "promotion_id": 0,
          "advert_status_id": 0
        }
      }
    },
    methods: {
      loadAdInfo: async function() {
        try {
          const resp = await axios.get(`http://localhost:8080/api/adverts/${this.$route.params.id}/`);
          this.ad = resp.data;
        } catch {
          this.$router.push('/ad-not-found')
        }
      }
    },
    created() {
      if(this.$route.params.id !== "0"){ //for dev purposes
        this.loadAdInfo();
      }
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

  .ad-title {
    font-size: 2.5rem;
    text-align: center;

    span {
      margin: 0 auto;
      font-size: 0.5em;
      color: #666;
    }
  }

  .description {
    margin: 20px;
    text-align: justify;
  }

  .city {
    font-size: 1rem;
    color: darkblue;
    margin: 0;
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
  }
</style>