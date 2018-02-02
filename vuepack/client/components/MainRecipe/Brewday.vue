<template>
  <div class="brewday">
      <hr>
      <h3>Brewday Assistant</h3>

      <div class="biab">
        <span class="infoBiab">BIAB Mode. 1 infusion step, no sparge. Select target temp. </span>
        <div class="biabStrike">
          <div class="biabWaterVol">
            <div><span>Target temp : </span> <input type="number" name="targetTemp" id="inputTargetTemp" :value="targetTemp" @input="biabTempUpdate"></div>
            <span>Added Water : </span> <span> {{ Math.round(recipe.biab.strikeVol * 10) / 10 }} L </span>
          </div>
          <div class="biabWaterTemp">
            <span>Water temperature : </span> <span> {{ temp }} °C </span>
          </div>
          <div class="biabRatio">
            <span>Ratio : </span> <span> {{ Math.round(recipe.biab.ratio * 10) / 10 }} </span>
          </div>
        </div>
      </div>
      <div class="preboil">
        <h4>Pre-Boil</h4>
        <div>Preboil volume (calculated) : </div>
        <div>Preboil gravity (calculated) :</div>
      </div>
      <div class="volumes">
        <h4>Volumes</h4>
        <div>Grain volume : </div>
        <div>Mash volume (first step) : </div>
        <div>Mash volume (last step) : </div>
      </div>

  </div>
</template>

<script>
export default {
  computed : {
    recipe () {
      return this.$store.state.selectedRecipe
    },
    targetTemp () {
      return this.$store.state.selectedRecipe.biab.targetTemp
    },
    temp : {
      get () {
        return this.$store.state.selectedRecipe.biab.temp

      }
    }
  },
  methods : {
    biabTempUpdate (e) {
      this.$store.commit('BIAB_TARGET_CHANGED', e.target.value)
    }
  }
}
</script>

<style>
hr {
  background-color: #515c66;
  margin-right: 100px;
}
.brewday {
  color: #ffffff;
}
.infoBiab {
  display: block;
  margin-top: 2rem;
}

.preboil {
  margin-top: 2rem;
}
.volumes {
  margin-top : 2rem;
}
</style>
