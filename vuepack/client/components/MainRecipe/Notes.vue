<template>
  <div class="notes">
      <h3>## Notes </h3>
      {{ notes }}
  </div>
</template>

<script>
export default {
    computed : {
        notes () {
            return this.$store.state.selectedRecipe.notes
        }
    }


}
</script>

<style>
 .notes {
   margin-top: 2rem;
   color: #fff;
 }
 .notes h3 {
   color:#4a4a4a;
 }
</style>
