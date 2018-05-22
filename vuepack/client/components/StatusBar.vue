<template>
  <div class="statusbar">
    <div class="brewday">
      <button>brewday mode</button>
    </div>
    <div class="beer-profile">
      <span>{{ recipe.ibu }} IBU</span>
      <span>{{ recipe.ebc }} EBC</span>
      <span>OG {{ recipe.og }}</span>
      <span>FG {{ recipe.fg }}</span>
      <span>BU/GU ratio {{ recipe.bugu }}</span>
      <span>Alc {{ recipe.alc }}%</span>
    </div>
  </div>
</template>

<script>
export default {
  computed : {
    recipe () {
      return this.$store.state.selectedRecipe
    }
  }
}
</script>

<style>
  .statusbar {
    position:fixed;
    left:0px;
    bottom:0px;
    padding:0;
    margin: 0;
    height:20px;
    width:100%;
    background:#14191f;
    font-size: 0.75rem;
  }

  .statusbar span {
    margin-left : 15px;
  }
  .beer-profile {
    float: right;
    margin-right: 35px;
  }
  .brewday button{
    float: left;
    background: #14191f;
    border:none;
    color:#39bae6;
  }
</style>
