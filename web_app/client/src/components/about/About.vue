<template>
  <div>
    <Navbar/>

    <!-- Header area -->
    <div class='about_header'>
      <h1 class='center'>About Me</h1>
    </div>
    <!-- End of Header Area -->

    <!-- Start of content area -->
    <div class='about_content_area'>

      <div class='pic_div'>
        <img src='../../assets/img/Cuddy.jpg'>
      </div>

      <div class='bio_div'>
        <p>
          In the spring of 2015, I chose to take a leap in a new direction and
          immerse myself in learning full stack web development. I attended the
          coding bootcamp Tech Talent South as well as Gwinnett Technical College
          for a degree in web development. Since then, I have fully immersed
          myself in the Atlanta tech community attending meetups, conferences as
          well as hackathons to grow as a developer. I’ve won first place two
          years in a row at the SkillsUSA state level, in web design, and competed
          at the national level. I’ve worked with Manning Publications to help
          review many of their books/videos on the latest technology trends. I
          continue to work to stay up to date with the latest technologies by
          using such resources as Team Treehouse and Udemy. My casual interest
          in web development has now become a guiding passion and I am excited
          to bring that passion to my next pursuit.
        </p>

        <p>
          The experience I have earned in the Marine Corps and C.I.A. has awarded
          me confidence and ability to be successful in any field. I’ve proven an
          ability to work well under pressure when I had three months to prepare
          40 Marines for a deployment to Camp Fallujah, Iraq. I’ve demonstrated
          communication skills was when I had to write a new convoy operations
          manual for the unit I served with in Afghanistan as well as giving 79
          convoy briefs in Iraq. My ability to plan has been established when I
          planned 15 convoys across South Korea moving over 1,000 pieces of decking,
          tents and aircraft equipment.
        </p>

        <p>
          I love meeting new people and inspiring innovative digital solutions,
          so feel free to send me an invite; I’d love to connect with you.
        </p>

      </div>

    </div>
    <!-- End of content area -->

  </div>
</template>

<script>
import Navbar from '@/components/support/Navbar';

export default {
  name: 'About',
  components: {
    Navbar,
  }
};
</script>

<style lang="css" scoped>
  .center {
    text-align: center;
  }
  .about_header {
    margin-top: 50px;
    margin-bottom: 50px;
  }
  img {
    border-radius: 10px;
    width: 80%;
  }
  .about_content_area {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 1em;
    margin-bottom: 50px;
    margin-left: 2%;
    margin-right: 2%;
  }
  @media only all and (max-width: 768px) {
    .pic_div {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .about_content_area {
      grid-template-columns: 1fr;
      margin-left: 2%;
      margin-right: 2%;
    }
  }
</style>
