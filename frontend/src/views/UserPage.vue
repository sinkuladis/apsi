<template>
  <div class="main-body">
    <h1>Panel osobisty</h1>
    <v-container style="max-width: 60%" ma-2>
      <v-row>
          <v-col cols="12">
              <v-text-field dense outlined v-model="user.username" label="Nick">
              </v-text-field>
          </v-col>
          <v-col cols="12">
              <v-text-field dense outlined v-model="user.first_name" label="Imię">
              </v-text-field>
          </v-col>
          <v-col cols="12">
              <v-text-field dense outlined v-model="user.last_name" label="Nazwisko">
              </v-text-field>
          </v-col>
          <v-col cols="12">
              <v-text-field dense outlined v-model="user.email" label="Email">
              </v-text-field>
          </v-col>               
          <v-col cols="12">
              <v-text-field
                      dense
                      outlined
                      flat
                      label="Hasło"
                      :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="showPass ? 'text' : 'password'"
                      counter
                        v-model="user.password"
                      @click:append="showPass = !showPass">
              </v-text-field>
          </v-col>
      </v-row>
      <v-row justify="center">
          <v-col cols="6">
              <v-btn 
                  :ripple="false" 
                  block 
                  depressed 
                  v-on:click="changeUserData" 
                  dark color="light-blue">Aktualizuj dane</v-btn>
          </v-col>
          <v-col cols="12" v-if="error">
              <p class="error">Wystąpił błąd.</p>
          </v-col>
          <v-col cols="12" v-else-if="success">
              <p class="success">Dane zmienione poprawnie.</p>
          </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  

  export default {
    data() {
      return {
        user: {
          username: '',
          last_name: '',
          first_name: '',
          email: '',
          password: ''
        },
        error: false,
        success: false,
        showPass: false,
      }
    },
    methods: {
      loadUserInfo: async function() {
        try {
          const resp = await this.$http.get(`http://localhost:8080/api/users/${this.$route.params.id}/`);
          this.user = {
            ...resp.data,
            password: this.user.password
          };
        } catch {
          this.$router.push('/not-found')
        }
      },
      changeUserData: async function() {
        const data = this.user;
        try {
          await this.$http.put(`http://localhost:8080/api/users/${this.$route.params.id}/`,
                        {
                            "username": data.username,
                            "last_name": data.last_name,
                            "first_name": data.first_name,
                            "email": data.email,
                            "password": data.password
                        },
                        {
                            mode: 'cors', 
                            credentials: 'same-origin', 
                            headers: {
                                'Content-Type': 'application/json'
                            },
                        });
          this.error = false;
          this.success = true;
          this.loadUserInfo();
        } catch {
          this.error = true;
        }
      }
    },
    created() {
      this.loadUserInfo();
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
      margin: 20px auto;
      padding-bottom: 10rem;
  }
</style>