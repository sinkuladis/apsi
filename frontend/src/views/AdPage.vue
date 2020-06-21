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
        <p class="email"><strong>Mail ogłoszeniodawcy: </strong><a :href="'mailto:' + mail">{{mail}}</a></p>
        <p>
          <v-btn @click="observeAd">Obserwuj</v-btn>
        </p>
        <p>
          <v-btn v-if="this.$store.getters.user.id === ad.user.id" @click="editAd(ad.id)">Edytuj ogłoszenie</v-btn>
        </p>
      </v-col>
    </v-row>
    <p class="description">{{ad.description}}</p>
    <v-snackbar v-model="snackBar.show" :timeout="2000">
      {{ snackBar.text }}
      <v-btn
              color="blue"
              text
              @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
      return {
        snackBar: {
          show: false,
          text: 'Wystąpił błąd!'
        },
        mail: '',
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
          "advert_status_id": 0,
          "advertiser_email": ""
        }
      }
    },
    methods: {
      loadAdInfo: async function() {
        try {
          const resp = await this.$http.get(`/api/adverts/${this.$route.params.id}/`);
          this.ad = resp.data;
          await this.loadAdvertiserMail()
        } catch {
          this.$router.replace('/ad-not-found')
        }
      },
      redirectToSeller: function(id) {
          this.$router.push(`/user/${id}/ads`)
      },
      editAd: function(id) {
        this.$router.push(`/ad/${id}/edit/`)
      },
      observeAd: async function() {
        this.$http({
                method: 'POST',
                url: `/api/adverts/${this.$route.params.id}/observed/`,
                data: {id: this.$route.params.id},
                credentials: 'include',
                headers: {'Authorization': 'Bearer ' + this.$store.getters.token}
        }).then(() => {
          this.snackBar.text = 'Dodano do obserwowanych'
          this.snackBar.show = true
        }).catch(() => {
          this.snackBar.text = 'Wystąpił błąd!'
          this.snackBar.show = true
        })
      },
      loadAdvertiserMail: async function() {
          await axios({
            method: 'GET',
            url: `/api/users/${this.ad.user.id}`,
            credentials: 'include',
            headers: {'Authorization': 'Bearer ' + this.$store.getters.token}
          }).then((response) => {
            this.mail = response.data.email
          }).catch(() => {
            this.mail = "Nie znaleziono"
          })
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

  .email {
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
