<template>
  <v-container>
    <v-row class="list__cafes-title">
      <v-col>
        <h1 class="text-center text-h1">All humans in database</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="human in humans" :key="human.id" >
        <human-card :onDelete="deleteHuman" :onEdit="editHuman" :human="human"></human-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HumanCard from "~/components/HumanCard";

export default {
  async asyncData({$axios, params}) {
    try {
      let humans = await $axios.$get(`/humans/`);
      return {humans};
    } catch (e) {
      // todo Разобраться как работает Nuxt error, какие статус-коды он принимает (401, 403, 404)
      // return {humans: []};
    }
  },
  head() {
    return {
      title: "Humans list"
    };
  },
  components: {
    HumanCard
  },
  data() {
    return {
      humans: []
    };
  },
  methods: {
    deleteHuman(human_id) {
      try {
        this.$axios.$delete(`/humans/${human_id}/`)
          .then(res => {
            //todo Удаление элемента из списка посредством js
            console.log(this.humans);
          })

          .catch(err => {
            // todo Обработка ошибки
          })
      } catch (e) {
        console.log(e);
      }
    },
    editHuman(human_id){
      console.log(this.humans.find(el => el.id === human_id))
    }
  }
};
</script>
