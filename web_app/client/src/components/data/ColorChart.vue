<template>
  <div>

    <!-- This section will build the color chart -->
    <section>

      <h2 class='center font'>Quick Battle Study</h2>
      <p class='center font'>See Who Was Winning More Battles During a Time Period</p>

      <div class='colorChart'>
        <div
          class='colorChart center'
          style="background-color: gold; margin: 0; color: #a81cea;"
          :style="{width: percent + '%'}">
        </div>
      </div>

      <div class='data_div center' v-if='showDataArea'>
        <p>The Romans won battles {{ percent }}% of the time between the years
        {{ yearOne }} and {{ yearTwo }}</p>
      </div>

      <form @submit="submitYears">
        <p>{{ getData }}</p>
        <label>Year One</label>
        <input type="number" v-model='yearOne' name="yearOne" placeholder="Enter First Year">
        <label>Year Two</label>
        <input type="number" v-model="yearTwo" name="yearTwo" placeholder="Enter Second Year">
        <div>
          <button class="btn btn-primary font" type="submit">Submit</button>
        </div>
      </form>

      <!-- This works - keep for reference -->
      <!-- <p>{{ totalBattles }}</p> -->

    </section>
    <!-- End of color chart section -->

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
      if (this.yearOne < -113 || this.yearTwo >= 570){
        alert('Years must be between -113 B.C.E and 570 C.E.')
      }else if (this.yearOne == this.yearTwo){
        alert('The years must be seperated by at least a year')
      }else {
        this.showDataArea = true
        const colorChartData = {
          yearOne: this.yearOne,
          yearTwo: this.yearTwo,
        };
        this.fetchColorChartData(colorChartData);
      }
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
