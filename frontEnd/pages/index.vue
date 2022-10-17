<template>
  <v-container>
    <v-row class="list__cafes-title">
      <v-col cols="6">
        <h1 class="text-h1">All humans</h1>
      </v-col>
      <v-col cols="6" class="flex-row justify-center">
        <human-add-dialog :roles="roles"/>
        <v-btn class="v-btn">Change roles</v-btn>
        <human-deleted-cart/>
        <v-select
          v-model="married"
          :items="selectItemsMarried"
          item-value="value"
          item-text="name"
          chips
          label="Set status married"
        />
        <v-select
          v-model="sex"
          :items="selectItemsSex"
          chips
          label="Set sex"
          multiple
        />
      </v-col>

    </v-row>
    <v-row>
      <v-col class="col-md-4 col-sm-6" v-for="human in filteredHumans()" :key="human.id">
        <human-editing-card v-if="editing.includes(human.id)" :human="human" :roles="roles"/>
        <human-card v-else :human="human"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HumanCard from "../components/HumanCard";
import HumanAddDialog from "../components/HumanAddDialog";
import HumanEditingCard from "../components/HumanEditingCard";
import HumanDeletedCart from "../components/HumanDeletedCart";

export default {
  //TODO
  //401 - запрос не был применён, поскольку ему не хватает действительных учётных данных для целевого ресурса.
  //403 - доступ запрещён и привязан к логике приложения
  //404 - сервер не может найти запрошенный ресурс

  async asyncData({$axios, error}) {
    let humans = await $axios.$get(`/humans/`)
      .catch(err => {
        error({
          statusCode: err.response.status,
          message: err.response.data ? err.response.data : err.response.statusText
        })
      });
    return {humans};
  },
  head() {
    return {
      title: "Humans list"
    };
  },
  components: {
    HumanDeletedCart,
    HumanAddDialog,
    HumanCard,
    HumanEditingCard
  },
  data() {
    return {
      selectItemsMarried: [
        {name: 'Is married', value: true},
        {name: 'Is not married', value: false}
      ],
      selectItemsSex: [
        'Women',
        'Men',
        'Middle'
      ],
      sex: '',
      married: [],
      humans: [],
      roles: [],
      editing: [],
      deleted: []
    };
  },
  methods: {
    checkMarried(human) {
      if (this.married.length === 0) return true;
      return this.married === human.is_married;
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
