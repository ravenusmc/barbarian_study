<template>
  <div>
      <nav class="navbar navbar-expand-lg navbar-custom navbar-static-top">
        <button class="navbar-toggler" type="button" data-toggle="collapse"
        data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
        aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/Map">Map</router-link>
            </li>
            <!-- <li class="nav-item">
              <router-link class="nav-link" to="/Graph">Graphs</router-link>
            </li> -->
            <li class="nav-item">
              <router-link class="nav-link" to="/About">About</router-link>
            </li>
          </ul>
        </div>
      </nav>
  </div>
</template>

<script>
export default {
};
</script>

<style>
/* change the background color */
.navbar-custom {
    background-color: #28566c;
}
/* change the brand and text color */
.navbar-custom .navbar-brand,
.navbar-custom .navbar-text {
    color: rgba(255,255,255,.8);
}
/* change the link color */
.navbar-custom .navbar-nav .nav-link {
    color: rgba(255,255,255,.5);
}
/* change the color of active or hovered links */
.navbar-custom .nav-item.active .nav-link,
.navbar-custom .nav-item:focus .nav-link,
.navbar-custom .nav-item:hover .nav-link {
    color: #ffffff;
}
</style>
