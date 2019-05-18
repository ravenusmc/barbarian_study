// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import { store } from './store/store';
import Chart from 'v-chart-plugin'

Vue.config.productionTip = false;

//This is needed for the chart
Vue.use(Chart);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
