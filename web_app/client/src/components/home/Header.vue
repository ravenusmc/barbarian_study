<template>
  <div id='main_div'>

    <div class='nav_div'>
      <div class='eagle_image'>
        <img class='spqr_eagle' src='../../assets/img/eagle3.jpg'>
      </div>
      <div class='sub_nav_div'>
        <ul>
          <li class="nav-item">
            <router-link class="font nav-link" to="/">HOME</router-link>
          </li>
          <li class="nav-item">
            <router-link class="font nav-link" to="/Data">DATA</router-link>
          </li>
          <li class="nav-item">
            <router-link class="font nav-link" to="/About">ABOUT</router-link>
          </li>
        </ul>
      </div>
      <div class='eagle_image'>
        <img src='../../assets/img/germanic.png'>
      </div>
    </div>

    <header>
      <img src='../../assets/img/barbarian_one.jpg'>
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
  grid-template-columns: 15% 85%;
}

/* .spqr_eagle {
  mix-blend-mode: multiply;
} */

img {
  width: 100%;
  height: auto;
}

.nav_div {
  background-color: #A91DEB;
}

.eagle_image {
  margin-top: 30%;
  background-color: rgba(0,0,0,0.5);
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

.sub_nav_div {
  margin-top: -205px;
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
  line-height: 50px;
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
