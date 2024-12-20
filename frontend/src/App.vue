<template>
  <div id="app">
    <Header />
    <SideMenu :user="user" />
    <MusicContainer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import SideMenu from "./components/SideMenu.vue";
import MusicContainer from "./components/MusicContainer.vue";

export default {
  name: "App",
  components: {
    Header,
    SideMenu,
    MusicContainer,
  },
  data() {
    return {
      user: null, // Replace with actual user data
    };
  },
};
</script>

<style>
body {
  font-family: "Jua", sans-serif;
}
</style>
