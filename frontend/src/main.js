import Vue from 'vue'
import router from '@/router/router'
import App from '@/App'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import vuetify from '@/plugins/vuetify'
import VueSession from 'vue-session'
import Axios from 'axios'
import store from './store'


Vue.use(VueMaterial)
Vue.use(VueSession)

Vue.prototype.$http = Axios;
Vue.prototype.$store = store;

const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
