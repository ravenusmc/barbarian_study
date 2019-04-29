<template>
  <div>

    <section>

      <h2 class='center font'>Quick Battle Study</h2>
      <p class='center font'>See Who Was Winning More Battles When</p>

      <div class='colorChart'>
      </div>

      <form @submit="submitYears">
        <label>Year One</label>
        <input type="number" v-model='yearOne' name="yearOne" placeholder="Enter First Year">
        <input type="number" v-model="yearTwo" name="yearTwo" placeholder="Enter Second Year">
        <div>
          <button class="btn btn-primary font" type="submit">Submit</button>
        </div>
      </form>

    </section>

  </div>
</template>

<script>
export default {
  name: 'ColorChart',
  data() {
    return {
      yearOne: 0,
      yearTwo: 0,
    }
  },
  methods: {
    submitYears(evt){
      evt.preventDefault();
      console.log('hi Mike')
      console.log({yearOne: this.yearOne})
    },
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

.colorChart {
  height: 150px;
  margin-left: 25%;
  margin-right: 25%;
  border: 2px solid red;
  background-color: #FFD700;
}

form {
  text-align: center;
  margin-top: 25px;
}

</style>
