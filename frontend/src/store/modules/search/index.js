import axios from "axios";

const state = {
    searchResult: [],
    status: ''
}

const mutations = {
    clearSearch(state){
        state.searchResult = []
    },
    storeSearch(state, result) {
        state.searchResult = result
    },
    searchError(state) {
        state.status = 'error'
    },
    searchSuccess(state) {
        state.status = 'success'
    }
}

const actions = {
    searchAdverts({commit}, data) {
        return new Promise((resolve, reject) => {
            axios({
                method: 'GET',
                url: '/api/adverts/',
                data: data
            }).then((response) => {
                commit('searchSuccess')
                commit('storeSearch', response.data)
                resolve(response)
            }).catch((error) => {
                commit('searchError')
                reject(error)
            })
        })
    }
}

const getters = {
    status: state => state.status,
    adverts: state => state.searchResult
}

const userModule = {
    state,
    mutations,
    actions,
    getters
}

export default userModule;
