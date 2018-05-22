<template>
  <div>
    <div class="columns">
      <!-- <counter></counter> -->
      <sidebar></sidebar>
      <mainRecipe></mainRecipe>
    </div>
   <statusBar></statusBar>
  </div>
</template>

<script>
import Sidebar from 'components/Sidebar'
import MainRecipe from 'components/MainRecipe'
import StatusBar from 'components/StatusBar'

export default {
  components: {
    Sidebar,
    MainRecipe,
    StatusBar
    
  }
}
</script>
