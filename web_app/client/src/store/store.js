import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export const store = new Vuex.Store({

  state: {
    colorChartData: {},
    graphOneData: {},
  },

  getters: {
    colorChartData: state => state.colorChartData,
    graphOneData: state => state.graphOneData,
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
      fetchGraphOneData: ({commit}) => {
        const path = 'http://localhost:5000/graphOne';
        axios.get(path)
        .then((res) => {
          console.log(res.data)
          commit('setGraphOneData', res.data);
        })
      }
  },

  mutations: {
    setColorChartData(state, data) {
      state.colorChartData = data;
    },
    setGraphOneData(state, data) {
      state.graphOneData = data
    }
  },

})
