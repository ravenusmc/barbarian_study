<template>
  <div>

    <div>
      <h2 class='font center'>Looking at Roman Victories by  Intervals</h2>
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
  methods: {
    ...mapActions([
      'fetchGraphOneData',
    ]),
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
