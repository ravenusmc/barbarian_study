<template>
  <div>
    <Navbar/>
    <Header/>
    <ColorChart/>
    <ChartOne/>


  </div>
</template>

<script>
import Navbar from '@/components/support/Navbar';
import Header from '@/components/data/Header';
import ColorChart from '@/components/data/ColorChart.vue';
import ChartOne from '@/components/data/GraphOne.vue';

export default {
  name: 'Data',
  components: {
    Navbar,
    Header,
    ColorChart,
    ChartOne,
  }
}
</script>

<style scoped>
</style>
