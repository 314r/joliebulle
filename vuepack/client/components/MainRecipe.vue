<template>
  <div class="column is-four-fifths main-view">
    <div class="name" v-on:click='toggleEditName()' >{{ recipe.name }}</div>
    <div v-if='editName === true'>yo</div>
    <div class="brewer is-size-7">a {{ recipe.style.name }} by {{ recipe.brewer }}</div>
    <ingredients></ingredients>
    <profile></profile>
    <notes></notes>
    <brewday></brewday>
  </div>
</template>

<script>
import Ingredients from 'components/MainRecipe/Ingredients'
import Profile from 'components/MainRecipe/Profile'
import Notes from 'components/MainRecipe/Notes'
import Brewday from 'components/MainRecipe/Brewday'


  export default {
    data () {
      return {
        editName : false
      }
    },
    computed : {
        recipe () {
          return this.$store.state.selectedRecipe
          }

    },
    components : {
      Ingredients,
      Profile,
      Notes,
      Brewday
    },
    methods : {
      toggleEditName : function () {
        return this.editName = !this.editName
      }

    }
  
}
</script>

<style>
.main-view  {
  padding-left : 75px;
  font-size: 14px;
}

.name {
  padding-top : 30px;
  color : #f29718;
  font-weight: 700;
}
.brewer {
  color : #39bae6;
}

</style>



