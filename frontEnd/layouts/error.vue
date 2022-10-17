<template>
  <v-app dark>
    <h1>
      {{error.statusCode}}
    </h1>
    <h2>
      {{error.message}}
    </h2>
  </v-app>
</template>

<script>
export default {
  name: 'EmptyLayout',
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    },
  },
  head () {
    const title = this.error.statusCode
    return {
      title
    }
  }
}
</script>

<style scoped>
h1 {
  width: 100%;
  text-align: center;
  font-size: 20px;
}
</style>
