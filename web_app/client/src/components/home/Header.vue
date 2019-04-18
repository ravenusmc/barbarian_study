<template>
  <div id='main_div'>

    <div class='nav_div'>
      <ul>
        <li class="nav-item">
          <router-link class="font nav-link" to="/">HOME</router-link>
        </li>
        <li class="nav-item">
          <router-link class="font nav-link" to="/About">ABOUT</router-link>
        </li>
      </ul>
    </div>

    <header>
      <img src='../../assets/img/barbarian_one.jpg'>
      <!-- <div class='title_div'>
        <h2>Barbarian Study</h2>
      </div> -->
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

img {
  width: 100%;
  height: auto;
}

/* header {
  width: 100%;
  height: auto; */
  /* height: 650px; */
  /* object-fit: contain; */
  /* background-image: url('../../assets/img/barbarian_one.jpg'); */
  /* background-size: contain; */
  /* background-size: 100%;
  background-repeat: no-repeat;
  background-position: center; */
/* } */

.nav_div {
  background-color: #A91DEB;
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

ul {
  list-style-type: none;
  color: black;
  margin-top: 250px;
}
a {
  color: #FFF;
  font-size: 30px;
  text-decoration: none;
  line-height: 30px;
}

a:hover {
  color: #FFCC33;
  text-decoration: none;
}

@media only all and (max-width: 768px){

  #main_div {
    grid-template-columns: 1fr;
  }

}


</style>
