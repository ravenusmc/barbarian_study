<template>
  <div>
    <Navbar/>
    <Header/>
    <ColorChart/>


  </div>
</template>

<script>
import Navbar from '@/components/support/Navbar';
import Header from '@/components/data/Header';
import ColorChart from '@/components/data/ColorChart.vue';

export default {
  name: 'Data',
  components: {
    Navbar,
    Header,
    ColorChart,
  }
}
</script>

<style scoped>
</style>
