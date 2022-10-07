<template>
  <main class="container my-5">
    <v-row>
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ human.first_name }}</h2>
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitHuman">
          <div class="form-group">
            <label for>First name:</label>
            <input type="text" class="form-control" v-model="human.first_name">
          </div>
          <div class="form-group">
            <label for>Last name:</label>
            <input v-model="human.last_name" type="text" class="form-control">
          </div>
          <div class="form-group">
            <label for>Patronymic:</label>
            <input v-model="human.patronymic" type="text" class="form-control">
          </div>
          <div class="form-group">
            <label for>Age:</label>
            <input v-model="human.age" type="number" class="form-control">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Sex:</label>
                <select v-model="human.sex" class="form-control">
                  <option value="Men">Men</option>
                  <option value="Women">Women</option>
                  <option value="Middle" selected>Middle</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>Married:</label>
                <select v-model="human.is_married" class="form-control">
                  <option value="Y">Yes</option>
                  <option value="N" selected>No</option>
                </select>
              </div>
            </div>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </v-row>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "Edit Recipe"
    }
  },
  async asyncData({$axios, params}) {
    try {
      let human = await $axios.$get(`/humans/${params.id}`);
      return {human};
    } catch (e) {
      return {human: []};
    }
  },
  data() {
    return {
      human: {
        first_name: "",
        last_name: "",
        patronymic: "",
        age: 0,
        sex: "Middle",
        is_married: "Y",
        role_id: 0
      }
    };
  },
  methods: {
    submitHuman() {
      let editedRecipe = this.human
      const config = {
        headers: {"content-type": "multipart/form-data"}
      };


      try {
        this.$axios.$patch(`/humans/${editedRecipe.id}/`, {human: this.human}, config)
          .then(res => {
            //todo
            })
          .catch(err => {
              //todo
            });

        this.$router.push("/humans/");
      } catch (e) {
        console.log(e);//todo
      }
    }
  }
};
</script>

<style scoped>
</style>
