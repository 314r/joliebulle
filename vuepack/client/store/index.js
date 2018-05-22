import Vue from 'vue'
import Vuex from 'vuex'
// import * as translate from '../lib/translate'
import * as beerCalc from '../lib/beercalc'

const ipcRenderer = require('electron').ipcRenderer

Vue.use(Vuex)

const state = {
  count: 0,
  recipes: [],
  config: {},
  selectedRecipe: {
    name: '',
    style: {},
    mash: {},
    biab: {
      targetTemp: 67,
      strikeVol: 0,
      temp: 0,
      ratio: 0
    }
  }
}

const mutations = {
  SET_RECIPES (state, data) {
    state.recipes = data
    console.log(data)
  },
  SET_CONFIG (state, data) {
    state.config = data
  },
  SET_SELECTED (state, recipe) {
    // recipe = translate.translate_en(recipe)
    recipe.ebc = Math.round(beerCalc.ebc(recipe.fermentables, recipe.batch_size))
    recipe.og = (Math.round(beerCalc.originalGravity(recipe) * 1000) / 1000).toFixed(3)
    recipe.fg = (Math.round(beerCalc.finalGravity(recipe) * 1000) / 1000).toFixed(3)
    recipe.ibu = Math.round(beerCalc.ibus(recipe).ibu)
    recipe.bugu = Math.round(beerCalc.bugu(recipe) * 10) / 10
    recipe.alc = Math.round(beerCalc.alc(recipe) * 10) / 10
    recipe.preboilVolume = beerCalc.preBoilCalc(state.config.General.CoolingLoss / 100, state.config.General.BoilOffRate / 100, recipe.boil_time, recipe.batch_size)
    recipe.preboilGravity = beerCalc.preBoilSgCalc(beerCalc.preBoilGu(recipe), recipe.batch_size, recipe.preboilVolume)
    recipe.grainWeight = beerCalc.weight(recipe.fermentables)
    recipe.grainVolume = beerCalc.grainVolumeCalc(recipe.grainWeight)
    // recipe.mashVolumeStrike = STEPS VOLUME NEEDED
    recipe.biab = beerCalc.biabCalc(recipe.preboilVolume, recipe.grainWeight, state.config.General, state.selectedRecipe.biab.targetTemp)
    console.log(recipe)
    state.selectedRecipe = recipe
  },

  BIAB_TARGET_CHANGED (state, newTemp) {
    state.selectedRecipe.biab.targetTemp = parseFloat(newTemp)
    const newBiab = beerCalc.biabCalc(state.selectedRecipe.preboilVolume, state.selectedRecipe.grainWeight, state.config.General, state.selectedRecipe.biab.targetTemp)
    // state.selectedRecipe.biab = newBiab
    Vue.set(state.selectedRecipe, 'biab', newBiab)
  }
}

const actions = {
  initRecipes ({ commit }) {
    ipcRenderer.on('initRecipes', function (event, data) {
      commit('SET_RECIPES', data)
    })
  },

  initConfig ({ commit }) {
    ipcRenderer.on('initConfig', function (event, data) {
      commit('SET_CONFIG', data)
    })
  }

}

const store = new Vuex.Store({
  state,
  mutations,
  actions
})

export default store
