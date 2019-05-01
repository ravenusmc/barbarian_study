<template>
  <div>

    <section>

      <h2 class='center font'>Quick Battle Study</h2>
      <p class='center font'>See Who Was Winning More Battles During a Time Period</p>

      <div class='colorChart'>
      </div>

      <form @submit="submitYears">
        <label>Year One</label>
        <input type="number" v-model='yearOne' name="yearOne" placeholder="Enter First Year">
        <label>Year Two</label>
        <input type="number" v-model="yearTwo" name="yearTwo" placeholder="Enter Second Year">
        <div>
          <button class="btn btn-primary font" type="submit">Submit</button>
        </div>
      </form>

    </section>

  </div>
</template>

<script>
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  name: 'ColorChart',
  data() {
    return {
      yearOne: 0,
      yearTwo: 0,
    }
  },
  methods: {
    ...mapActions([
      'fetchColorChartData',
    ]),
    submitYears(evt){
      evt.preventDefault();
      const colorChartData = {
        yearOne: this.yearOne,
        yearTwo: this.yearTwo,
      };
      this.fetchColorChartData(colorChartData);
      console.log({yearOne: this.yearOne, yearTwo: this.yearTwo})
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
