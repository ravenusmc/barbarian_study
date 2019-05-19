<template>
  <div>

    <div>
      <h2 class='font center'>Looking at Roman Victories by  Intervals</h2>
    </div>

    <div>
     <v-chart :chartData="adjustData"></v-chart>
     <div>
     </div>
    </div>

  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';
//Will use 75 yearly intervals for break down -700 year stretch from -130 BCE to 569 CE.

export default {
  name: 'ChartOne',
  data() {
    return {
      height: 600,
      width: 600,
      xAxisLabels: ['1','2','3','4','5','6','7','8','9','10'],
      vBarChartData: [],
    }
  },
  methods: {
    ...mapActions([
      'fetchGraphOneData',
    ]),
  },
  computed: {
    ...mapGetters([
      'graphOneData',
    ]),
    adjustData() {
      return this.vBarChartData = {
        chartType: "vBarChart",
        label: true,
        fill: 'green',
        selector: "vChart",
        title: "Roman Victories",
        subtitle: "By 75 Year Intervals",
        width: 500,
        height: 500,
        metric: ["Roman Victories", 'Total Battles'],
        dim: "Interval",
        data: this.graphOneData,
        grid: {
  enabled: true,
  gridTicks: 25,
},
        overrides: {
          palette: {
            fill: ['#A91DEB', '#4fc08d'],
            stroke: '#41B883'
          },
          x: {
            ticks: 20
          },
          y: {
            axisWidth: 40,
          },
        },
        legends: {
          enabled: true,
          height: 5,
          width: 50,
        },
      }
    },
  },
  mounted() {
    this.fetchGraphOneData()
  },
}
</script>

<style scoped>
.font {
  font-family: 'Cinzel', serif;
  margin-top: 50px;
}

.center {
  text-align: center;
}
</style>
