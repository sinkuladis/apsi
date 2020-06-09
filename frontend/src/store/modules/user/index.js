import axios from "axios";

const state = {
    status: '',
    token: localStorage.getItem('token') || '',
    user : {}
}

const mutations = {
    auth_request(state){
        state.status = 'loading'
    },
    auth_success(state, token){
        state.status = 'success'
        state.token = token
    },
    auth_error(state){
        state.status = 'error'
    },
    user_data_request(state){
        state.status = 'loading'
    },
    user_data_success(state, user){
        state.status = ''
        state.user = user
    },
    user_data_error(state){
        state.status = 'error'
        state.user = {}
    },
    update_user_data_request(state){
        state.status = 'loading'
    },
    update_user_data_success(state, user){
        state.status = ''
        state.user = user
    },
    update_user_data_error(state){
        state.status = 'error'
    },
    logout(state){
        state.status = ''
        state.token = ''
        state.user = {}
    },
}

const actions = {
    login({commit, dispatch}, user){
        return new Promise((resolve, reject) => {
            commit('auth_request')
            axios({url: '/api/token/', data: user, method: 'POST' })
                .then((resp) => {
                    const token = resp.data.access
                    localStorage.setItem('token', token)
                    axios.defaults.headers.common['Authorization'] = token
                    commit('auth_success', token)
                    dispatch('getUserData', token).then(() => {
                        resolve(resp)
                    })
                }).catch((e) => {
                commit('auth_error')
                localStorage.removeItem('token')
                reject(e)
            })
        })
    },
    register({commit}, user){
        return new Promise((resolve, reject) => {
            commit('auth_request')
            axios({url: '/api/users/', data: user, method: 'POST' })
                .then((resp) => {
                    commit('auth_success')
                    resolve(resp)
                }).catch((e) => {
                commit('auth_error', e)
                localStorage.removeItem('token')
                reject(e)
            })
        })
    },
    logout({commit}){
        return new Promise((resolve) => {
            commit('logout')
            localStorage.removeItem('token')
            delete axios.defaults.headers.common['Authorization']
            resolve()
        })
    },
    getUserData({commit}, token){
        return new Promise((resolve, reject) => {
            commit('user_data_request')
            axios.get("/api/users/current",
                {
                    credentials: "include",
                    headers: {'Authorization': 'Bearer ' + token}
                }).then(resp => {
                const userdata = resp.data
                commit('user_data_success', userdata)
                resolve(resp)
            }).catch((e) => {
                commit('user_data_error', e)
                reject(e)
            })
        })
    },
    updateUserData({commit}, data){
        return new Promise((resolve, reject) => {
            commit('update_user_data_request')
            axios({url: `/api/users/${data.id}/`, data: data, method: 'PUT'})
                .then((resp) => {
                    commit('update_user_data_success', resp.data)
                    resolve(resp)
                }).catch((e) => {
                commit('update_user_data_error')
                reject(e)
            })
        })
    }
}

const getters = {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    user: state => state.user
}

const userModule = {
    state,
    mutations,
    actions,
    getters
}

export default userModule;
