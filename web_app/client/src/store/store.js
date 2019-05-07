import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export const store = new Vuex.Store({

  state: {
    colorChartData: {},
  },

  getters: {
    colorChartData: state => state.colorChartData,
  },

  actions: {
      fetchColorChartData: ({ commit }, payload) => {
        const path = 'http://localhost:5000/colorChart';
        axios.post(path, payload)
        .then((res) => {
          commit('setColorChartData', res.data)
        })
        .catch((error) => {
          console.log(error);
        });
      },
    },

  mutations: {
    setColorChartData(state, data) {
      state.colorChartData = data;
    },
  },

})
