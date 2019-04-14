<template>
  <div id="app">
    <Navbar/>
      <router-view/>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/support/Navbar';
import Footer from '@/components/support/Footer';
export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
  }
};
</script>

<style>
</style>
