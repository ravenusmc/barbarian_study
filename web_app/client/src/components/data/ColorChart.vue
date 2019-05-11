<template>
  <div>

    <section>

      <h2 class='center font'>Quick Battle Study</h2>
      <p class='center font'>See Who Was Winning More Battles During a Time Period</p>

      <div class='colorChart'>
        <div
          class='colorChart center'
          style="background-color: gold; margin: 0; color: #a81cea;"
          :style="{width: percent + '%'}">
          {{ percent }}
        </div>
      </div>

      <div class='data_div center' v-if='showDataArea'>
        <p>The Romans won battles {{ percent }}% of the time</p>
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

      <p>{{ getData }}</p>
      <!-- This works -->
      <p>{{ totalBattles }}</p>


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
      totalBattles: 0,
      romanWins:0,
      percent: 0,
      showDataArea: false
    }
  },
  computed: {
    ...mapGetters([
      'colorChartData',
  ]),
  getData() {
    this.totalBattles = this.colorChartData.Total
    this.romanWins = this.colorChartData.Roman_Victories
    this.percent = (this.romanWins / this.totalBattles) * 100
    this.percent = new Intl.NumberFormat('en-US', { maximumSignificantDigits: 4 }).format(this.percent)
    }
  },
  methods: {
    ...mapActions([
      'fetchColorChartData',
    ]),
    submitYears(evt){
      evt.preventDefault();
      this.showDataArea = true
      const colorChartData = {
        yearOne: this.yearOne,
        yearTwo: this.yearTwo,
      };
      this.fetchColorChartData(colorChartData);
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

.data_div {
  margin-top: 25px;
}

.colorChart {
  border-radius: 5px;
  height: 150px;
  margin-left: 25%;
  margin-right: 25%;
  background-color: #a81cea;
  transition: width 500ms;
}

form {
  text-align: center;
  margin-top: 25px;
}

</style>
