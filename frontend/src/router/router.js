import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title: 'Homepage'
        }
    }
]

Vue.use(VueRouter);

export default new VueRouter({
    routes
})
