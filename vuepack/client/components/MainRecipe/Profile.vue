<template>
  <div class="mash-profile">
      <h3>## Mash Profile</h3>
      <div class="mash-name">{{ mash.name }}</div>
      <div class="mash-ph">pH : {{ mash.ph }}</div>
      <div v-for="step in mash.mash_steps">
          <span> {{ step.name }} </span>
          <span> {{ step.type }}</span>
          <span> @ {{ step.step_temp }} °C</span>
          <span> -> {{ step.step_time }} min</span>
      </div>
      <div class="mash-sparge"> Sparge : {{ mash.sparge_temp }} °C</div>
  </div>
</template>

<script>
export default {
    computed : {
        mash () {
          return this.$store.state.selectedRecipe.mash
          }
    }

}
</script>

<style>
 .mash-profile {
   margin-top: 2rem;
   color: #fff;
 }
 .mash-profile h3 {
   color:#4a4a4a;
 }
 .mash-name {
   color: #39bae6;
 }
</style>
