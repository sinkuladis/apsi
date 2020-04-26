import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home'
import Login from "@/views/Login";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title: 'Homepage'
        }
    },
    {
        path: '/login',
        name: 'Logowanie',
        component: Login,
    }
]

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    routes
})
