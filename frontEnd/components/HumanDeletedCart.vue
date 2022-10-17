<template>
  <v-dialog max-width="600px" scrollable>
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="text--black" v-bind="attrs" v-on="on" @click="deletedHumans()">
        Return deletes
      </v-btn>
    </template>
    <v-card v-for="human in this.$parent.deleted">
      <v-card-text v-for="field in humanFields(human)" class="v-card__text">
        <strong>{{ field.key }}</strong> {{ field.value }}
      </v-card-text>
      <v-card-actions>
        <v-btn color="green" text @click="addDeletedHuman()">
          Return
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "HumanDeletedCart",

  methods: {
    deletedHumans() {
      if (Object.keys(this.$parent.deleted).length === 0) {
        this.$axios.$get(`/deleted/`)
          .catch(err => {
            this.$nuxt.error({
              statusCode: err.response.status,
              message: err.response.data ? err.response.data : err.response.statusText
            })
          })
          .then(res => {
            this.$parent.deleted = res
          });
      }
    },
    humanFields(human) {
      let mappedHuman = Object.keys(human).map(key => ({key, value: human[key]}));
      mappedHuman.splice(0, 1);
      return mappedHuman;
    }
  }
}
</script>

<style scoped>

</style>
