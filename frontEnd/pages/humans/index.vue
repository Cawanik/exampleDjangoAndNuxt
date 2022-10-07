<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>Людишки</h3>
          <nuxt-link to="/humans/add" class="btn btn-info">Add Human</nuxt-link>
        </div>
      </div>
      <div v-for="human in humans" :key="human.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
        <human-card :onDelete="deleteHuman" :human="human"></human-card>
      </div>
    </div>
  </main>
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
    async deleteHuman(human_id) {
      try {
        this.$axios.$delete(`/humans/${human_id}/`)
          .then(res => {
            //todo Удаление элемента из списка посредством js
            })

          .catch(err => {
            // todo Обработка ошибки
          })
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
