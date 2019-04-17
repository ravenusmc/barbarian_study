<template>
  <div id='main_div'>
    <div>
    </div>
    <header>
      <div class='title_div'>
        <h2>Barbarian Study</h2>
      </div>
    </header>
  </div>
</template>

<script>
  export default {
    name: 'Header',
  }
</script>

<style scoped>

#main_div {
  display: grid;
  grid-template-columns: 20% 80%;
}

header {
  height: 650px;
  object-fit: contain;
  background-image: url('../../assets/img/barbarian_one.jpg');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right center;
}

.title_div {
  height: 650px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
}

h2 {
  background: rgba(235, 201, 29, 0.8);
  padding: 20px;
  border-radius: 15px;
}
</style>
