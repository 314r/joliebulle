<template>
  <div class="column sidebar">
    <ul>
        <li v-for='(recipe, index) in recipes' :key=recipe.path v-bind:class="{highlighted:index == selected}" v-on:click='recipeSelected(recipe,index)'>{{recipe.name}}</li>
    </ul>
  </div>  
</template>

<script>
export default {
  data () {
    return {
      selected: -1
    }
  },
  computed : {
      recipes () {
          return this.$store.state.recipes
      }
  },
  methods : {
      recipeSelected : function (recipe, index) {
          this.$store.commit('SET_SELECTED', recipe);
          this.selected = index;
          }
  }
}
</script>

<style>
.sidebar {
  padding-top: 30px;
  padding-left: 20px;
  font-size: 0.75rem;
  color: #515c66;
}

.sidebar li {
  padding-left:15px;

}

li.highlighted {
  background-color: #191f26;
  color: #e6e1cf;
}

</style>


