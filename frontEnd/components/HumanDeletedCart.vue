<template>
  <v-dialog max-width="600px" scrollable>
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="text--black" v-bind="attrs" v-on="on" @click="deletedHumans()">
        Return deletes
      </v-btn>
    </template>
    <v-card v-for="human in deleted" :key="deleted.id">
      <v-card-text v-for="field in humanFields(human)" class="v-card__text">
        <strong>{{ field.key }}</strong> {{ field.value }}
      </v-card-text>
      <v-card-actions>
        <v-btn color="green" text @click="returnHuman(human.id)">
          Return
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "HumanDeletedCart",

  props: {
    deleted: {
      type: Array,
      required: true
    }
  },

  methods: {
    returnHuman(id) {
      this.$emit('return');
    },
    humanFields(human) {
    }
  }
}
</script>

<style scoped>

</style>
