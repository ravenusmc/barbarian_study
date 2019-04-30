import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export const store = new Vuex.Store({

  state: {
    graphOneData: [],
  },

  getters: {
    graphOneData: state => state.graphOneData,
  },

  actions: {
      fetchGraphOneData: ({ commit }, payload) => {
        const path = 'http://localhost:5000/incidents_per_year';
        axios.post(path, payload)
        .then((res) => {
          commit('setGraphOneData', res.data)
        })
        .catch((error) => {
          console.log(error);
        });
      },
    },

  mutations: {
    setGraphOneData(state, data) {
      state.graphOneData = data;
    },
  },

})
