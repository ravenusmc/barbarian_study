<template>
  <div>

    <section>

      <h2 class='center font'>Quick Battle Study</h2>
      <p class='center font'>See Who Was Winning More Battles When</p>

      <div class='colorChart'>
      </div>

      <form>
      </form>

    </section>

  </div>
</template>

<script>
export default {
  name: 'ColorChart',
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

section {
}

.colorChart {
  height: 150px;
  margin-left: 25%;
  margin-right: 25%;
  border: 2px solid red;
  background-color: #FFD700;
}

</style>
