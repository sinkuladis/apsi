import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Login from "@/views/Login"
import SubmitAdvert from "@/views/Adverts/SubmitAdvert"
import AdPage from '@/views/AdPage'
import AdNotFound from '@/views/AdNotFound'
import UserPage from '@/views/UserPage'
import NotFound from '@/views/NotFound'
import ObservedAds from '@/views/ObservedAds'
import store from '../store/store'
import UserAds from '@/views/UserAds'
import LastAddedAds from '@/views/LastAddedAds'

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
    },
    {
        path: '/ad/:id',
        name: 'Ogłoszenie',
        component: AdPage,
    },
    {
        path: '/ad/:id/edit',
        name: 'Edytowanie ogłoszenia',
        component: SubmitAdvert
    },
    {
        path: '/ad-not-found',
        name: 'Ogłoszenie nieznalezione',
        component: AdNotFound,
    },
    {
        path: '/user/:id/observed-ads',
        name: 'Obserwowane ogłoszenia',
        component: ObservedAds,
    },
    {
        path: '/user/:id/ads',
        name: 'Ogłoszenia',
        component: UserAds,
    },
    {
        path: '/userpage',
        name: 'Panel użytkownika',
        component: UserPage,
        meta: { requiresAuth: true }
    },
    {
        path: '/submit-advert',
        name: 'Dodanie ogłoszenia',
        component: SubmitAdvert,
    },
    {
        path: '/latest',
        name: 'Ostatnio dodane',
        component: LastAddedAds,
    },
    {
        path: '/not-found',
        name: 'Strona nie istnieje',
        component: NotFound,
    },
    {
        path: '*',
        redirect: '/'
    }
]

Vue.use(VueRouter);

const router = new VueRouter({
    mode: 'history',
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.getters.isLoggedIn) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router;
