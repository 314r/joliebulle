<template>
  <div class="ingredients-list">
    <h3>## Ingredients </h3>
    <div v-for="(fermentable,index) in recipe.fermentables" :key='index'>
      <div class="fermentable-name" v-on:click='toggleEditFermentable(index)'>{{ fermentable.name }} <span class="f-details">[ {{ Math.round(fermentable.color) }} ebc - {{fermentable.yield}}% yield ]</span></div>
      <div v-if='editFerm === true && index === selectedIndex'>yo</div>
      <span class="fermentable-amount">{{ fermentable.amount }} g</span>
      <span class="fermentable-mash">{{ fermentable.afterBoil }}</span>
    </div>

    <div v-for="hop in recipe.hops" >
      <span class="hop-name">{{ hop.name }}</span>
      <span class="hop-amount">{{ hop.amount }} g</span>
      <span class="hop-time">{{ hop.use }} - {{ hop.time }} min</span>
    </div>
    <div v-for="(misc, index3) in recipe.miscs" :key='index3'>
      <span class="misc-name">{{ misc.name }} {{ [misc.type] }} </span>
      <span class="misc-amount">{{ misc.amount }} g </span>
      <span class="misc-use">{{ misc.use }} - {{ misc.time }} min</span>
    </div>
    <div v-for="(yeast, index4) in recipe.yeasts"  :key='index4'>
      <span class="yeast-name">{{ yeast.name }}</span>
      <span class="yeast-atten">{{ yeast.attenuation }} % attenuation</span>
      <span class="yeast-form">{{yeast.form}}</span>
    </div>
  </div>

    
</template>

<script>
export default {
    data () {
      return {
        editFerm : false,
        selectedIndex : ''
      }
    },
    computed : {
        recipe () {
          return this.$store.state.selectedRecipe
          }
    },
    methods : {
      toggleEditFermentable : function (index) {
        this.editFerm = !this.editFerm
        this.selectedIndex = index
      }
    }

}
</script>

<style>
 .ingredients-list {
   margin-top: 2rem;
   color: #fff;
 }
 .ingredients-list h3 {
   color:#4a4a4a;
 }

.fermentable-name, .hop-name, .misc-name, .yeast-name {
  display: block; 
  margin-top:0.5em; 
}

.fermentable-amount, .hop-amount, .misc-amount, .yeast-atten {
  padding-right: 15px;
  color: #c2d94c;
}
.fermentable-mash, .hop-time, .misc-use, .yeast-form {
  padding-right: 15px;
  color: #e6b673;
}
.f-details {
  color:#4a4a4a;
}
</style>
