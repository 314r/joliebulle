<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
const ipcRenderer = require('electron').ipcRenderer;

export default {
  created () {
    ipcRenderer.send('load')
    this.$store.dispatch('initRecipes')
    ipcRenderer.send('loadConfig')
    this.$store.dispatch('initConfig')
    }
}
</script>


<style>

html {
  background-color: #0f1419;
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Roboto Mono', monospace;

}





</style>
