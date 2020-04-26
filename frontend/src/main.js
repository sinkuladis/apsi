import Vue from 'vue'
import router from '@/router/router'
import App from '@/App'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import vuetify from '@/plugins/vuetify'

Vue.use(VueMaterial)

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
