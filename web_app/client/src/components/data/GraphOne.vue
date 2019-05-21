<template>
  <div>

    <div>
      <h2 class='font center'>Looking at Roman Victories by Intervals</h2>
    </div>

    <section class='chartSection'>

      <div>
        <v-chart :chartData="buildGraph"></v-chart>
      </div>

      <div>
        <table>
          <tr>
            <th>Interval</th>
            <th>Years</th>
          </tr>
          <tr>
            <td>1</td>
            <td>-113 B.C.E to -38 B.C.E</td>
          </tr>
          <tr>
            <td>2</td>
            <td>-38 B.C.E to 37 C.E</td>
          </tr>
          <tr>
            <td>3</td>
            <td>37 C.E to 112 C.E</td>
          </tr>
          <tr>
            <td>4</td>
            <td>112 C.E to 187 C.E</td>
          </tr>
          <tr>
            <td>5</td>
            <td>187 C.E to 262 C.E</td>
          </tr>
          <tr>
            <td>6</td>
            <td>262 C.E to 337 C.E</td>
          </tr>
          <tr>
            <td>7</td>
            <td>337 C.E to 412 C.E</td>
          </tr>
          <tr>
            <td>8</td>
            <td>412 C.E to 487 C.E</td>
          </tr>
          <tr>
            <td>9</td>
            <td>487 C.E to 562 C.E</td>
          </tr>
          <tr>
            <td>10</td>
            <td>563 C.E to 637 C.E</td>
          </tr>
        </table>
      </div>

    </section>

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
    buildGraph() {
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

.chartSection {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

table {
  font-family: 'Cinzel', serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 6px;
  text-align: center;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
