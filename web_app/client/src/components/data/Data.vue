<template>
  <div>
    <Navbar/>
    <Header/>


  </div>
</template>

<script>
import Navbar from '@/components/support/Navbar';
import Header from '@/components/data/Header';

export default {
  name: 'Data',
  components: {
    Navbar,
    Header
  }
}
</script>

<style scoped>
</style>
