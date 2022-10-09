<template>
  <v-container>
    <v-row class="list__cafes-title">
      <v-col cols="6">
        <h1 class="text-h1">All humans</h1>
      </v-col>
      <v-col cols="6" class="flex-row justify-center">
        <human-add-dialog :roles="roles" :onAdd="addHuman"/>
        <v-btn class="v-btn">Change roles</v-btn>
        <v-select
          v-model="married"
          :items="[{name:'Is married', value: true}, {name:'Is not married', value: false}]"
          item-value="value"
          item-text="name"
          chips
          label="Set status married"
          multiple
        />
        <v-select
          v-model="sex"
          :items="['Women', 'Men', 'Middle']"
          chips
          label="Set sex"
          multiple
        />
      </v-col>

    </v-row>
    <v-row>
      <v-col class="col-md-4 col-sm-6" v-for="human in filteredHumans()" :key="human.id">
        <human-editing-card v-if="editing.includes(human.id)"
                            :onDelete="deleteHuman"
                            :onSubmit="editHumanComplete"
                            :human="human"
                            :roles="roles"
                            :onCancel="cancelEdit"
        />
        <human-card v-else
                    :roles="roles"
                    :onDelete="deleteHuman"
                    :onEdit="editHuman"
                    :human="human"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HumanCard from "../components/HumanCard";
import HumanAddDialog from "../components/HumanAddDialog";
import HumanEditingCard from "../components/HumanEditingCard";

export default {
  async asyncData({$axios, params}) {
    try {
      let humans = await $axios.$get(`/humans/`);
      let roles = await $axios.$get('/role/');
      return {humans, roles};
    } catch (e) {
      // todo Разобраться как работает Nuxt error, какие статус-коды он принимает (401, 403, 404)
    }
  },
  head() {
    return {
      title: "Humans list"
    };
  },
  components: {
    HumanAddDialog,
    HumanCard,
    HumanEditingCard
  },
  data() {
    return {
      humans: [],
      roles: [],
      editing: [],
      married: [],
      sex: [],
      humanExample: {
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
    deleteHuman(human_id) {
      this.$axios.$delete(`/humans/${human_id}/`)
        .then(res => {
          this.humans = this.humans.filter(el => {
            return el.id !== human_id
          })
        })
        .catch(err => {
          // todo Обработка ошибки
          console.log(err)
        })
    },
    addHuman(human) {
      this.$axios.$post(`/humans/`, human)
        .then(res => {
          this.humans.push(human);
        })
        .catch(err => {
          // todo Обработка ошибки
          console.log(err)
        })
    },
    editHuman(human_id) {
      this.editing.push(human_id);
    },
    editHumanComplete(human) {
      let humanId = human.id;

      this.$axios.$patch(`/humans/${humanId}/`, human)
        .then(res => {
          let indexEditingElement = this.humans.indexOf(this.humans.find(el => {
            return el.id === res.id;
          }));
          this.humans.splice(indexEditingElement, 1, res)
        })
        .catch(err => {
          // todo Обработка ошибки
          console.log(err)
        })
    },
    cancelEdit(human_id) {
      this.editing = this.editing.filter(el => {
        return el !== human_id;
      })
    },
    checkMarried(human) {
      if (this.married.length === 0) return true;
      return this.married.includes(human.is_married);
    },
    checkSex(human) {
      if (this.sex.length === 0) return true;
      return this.sex.includes(human.sex);
    },
    filteredHumans() {
      return this.humans.filter(human => {
        return this.checkMarried(human) && this.checkSex(human);
      });
    }
  },

}
</script>
