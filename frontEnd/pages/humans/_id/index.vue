<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ human.first_name }}</h2>
      </div>
      <div class="col-md-6">
        <div class="recipe-details">
          <h4>Last name</h4>
          <p>{{ human.last_name }}</p>
          <h4>Patronymic</h4>
          <p>{{ human.patronymic }}</p>
          <h4>Age</h4>
          <p>{{ human.age }} years</p>
          <h4>Sex</h4>
          <p>{{ human.sex }}</p>
          <h4 v-if="human.is_married==='Y'">Is married</h4>
          <h4 v-else>Is not married</h4>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "View Human"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let human = await $axios.$get(`/humans/${params.id}`);
      return { human };
    } catch (e) {
      return { human: [] }; //todo
    }
  },
  data() {
    return {
    };
  }
};
</script>

<style scoped>
</style>
