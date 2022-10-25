<template>
  <v-card class="v-card v-card--flat">
    <v-icon v-if="ageCheck" color="red" class="flag-warning" right>mdi-alert-circle</v-icon>
    <h5 class="v-card__title">{{ human.first_name }}</h5>

    <div v-for="human in humanFields" :key="human.key">
      <v-card-text class="v-card__text">
        <strong>{{ human.key }}</strong> {{ human.value }}
      </v-card-text>
    </div>

    <v-card-actions class="action-buttons">
      <v-btn @click="onEdit()" color="blue">
        Edit
      </v-btn>
      <v-btn @click="onDelete()" color="red">
        Delete
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {
  name: "HumanCard",

  props: {
    human: {
      type: Object,
      required: true
    }
  },

  data() {
    return {
      maxAgeWithoutWarning: 40
    };
  },

  computed: {
    ageCheck() {
      return this.human.age > this.maxAgeWithoutWarning
    },

    humanFields() {
      let mappedHuman = Object.keys(this.human).map(key => ({key, value: this.human[key]}));
      mappedHuman.splice(0, 1);

      return mappedHuman;
    }
  },

  methods: {
    onEdit() {
      this.$emit('edit');
    },

    onDelete() {
      this.$axios.$delete(`/humans/${this.human.id}/`)
        .then(res => {
          this.$emit('delete');
        })
        .catch(err => {
          console.log(err)
          this.$nuxt.error({
            statusCode: err.response.status,
            message: err.response.data ? err.response.data : err.response.statusText
          })
        })
    },
  }
};
</script>

<style scoped>
.flag-warning {
  position: absolute;
  top: 20px;
  right: 20px;
}
</style>
