<template>
  <v-card class="v-card v-card--flat">
    <v-icon v-if="ageCheck" color="red" class="flag-warning" right>mdi-alert-circle</v-icon>
    <h5 class="v-card__title">{{ human.first_name }}</h5>

    <div v-for="human in humanFields">
      <v-card-text class="v-card__text">
        <strong>{{ human.key }}</strong> {{ human.value }}
      </v-card-text>
    </div>

    <v-card-actions class="action-buttons">
      <v-btn @click="onEdit()" color="blue" class="v-btn">Edit</v-btn>
      <v-btn @click="onDelete()" color="red" class="v-btn">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
//todo 2) Собрать кастомный css внутри папки assets, 4) В формах сделать валидацию
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
      // TODO
      //entries не работает, так как есть булевы значения
      let mappedHuman = Object.keys(this.human).map(key => ({key, value: this.human[key]}));
      //удаление id
      mappedHuman.splice(0, 1);
      return mappedHuman;
    }
  },
  methods: {
    // TODO
    // Знаю, что такие комменты оставлять нельзя, они адресованы Александру Кислеру.
    // Я себе голову разбил, нихуя не понимаю, почему $nuxt не в ебанном контексте
    // Я прочитал, что error и другие методы nuxt доступны в некоторых жизненных циклах накста
    // Но я просто не понимаю, как правильно заинжектить это сюда

    onEdit() {
      this.$parent.editing.push(this.human.id);

      if (Object.keys(this.$parent.roles).length === 0)
        this.$axios.$get(`/role/`)
          .then(res => {
            this.$parent.roles = res;
          })
          .catch(err => {
            this.$nuxt.error({
              statusCode: err.response.status,
              message: err.response.data ? err.response.data : err.response.statusText
            });
          });
    },
    onDelete() {
      this.$axios.$delete(`/humans/${this.human.id}/`)
        .then(res => {
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
          this.$parent.deleted.append(this.$parent.humans.filter(el => {
            return el.id === this.human.id;
          }))
          this.$parent.humans = this.$parent.humans.filter(el => {
            return el.id !== this.human.id;
          })
        })
        .catch(err => {
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
