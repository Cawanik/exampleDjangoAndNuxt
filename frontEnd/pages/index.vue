<template>
  <v-container>
    <v-row class="list__cafes-title">
      <v-col cols="6">
        <h1 class="text-h1">All humans</h1>
      </v-col>
      <v-col cols="6" class="flex-row justify-center">
        <human-add-dialog
          v-on:add="human=>addCard(human)"
          :roles="roles"
        />
        <v-btn class="v-btn">Change roles</v-btn>
        <human-deleted-cart
          v-on:return="del=>returnDelete(del)"
          :deleted="deleted"
        />
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
      <v-col
        cols="4"
        v-for="human in filteredHumans()"
        :key="human.id"
      >
        <human-editing-card
          v-if="editing.includes(human.id)"
          v-on:delete="moveToDelete(human.id)"
          v-on:cancel="cancelEdit(human.id)"
          v-on:submit="editSubmit(human.id)"
          :human="human"
          :roles="roles"
        />
        <human-card
          v-else
          v-on:delete="moveToDelete(human.id)"
          v-on:edit="addEdit(human.id)"
          :human="human"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {

  async asyncData({$axios, error}) {
    let {humans, roles, deleted} = await $axios.$get(`/humans/`)
      .catch(err => {
        error({
          statusCode: err.response.status,
          message: err.response.data ? err.response.data : err.response.statusText
        })
      });

    return {humans, roles, deleted};
  },

  head() {
    return {
      title: "Humans list"
    };
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
    returnDelete(id){
      this.humans.push(this.deleted.find(del => del.id === id));
      this.deleted = this.deleted.filter(del => del.id !== id);
      this.cancelEdit(id)
    },

    addCard(human){
      human.role = this.roles.find(role=>role.id = human.role).name
      delete human.password
      delete human.email
      this.humans.push(human)
    },

    editSubmit(id) {
      this.cancelEdit(id);

      this.$axios.$get(`/humans/${id}`)
        .then(res => {
          this.humans[this.humans.findIndex(hum=>hum.id === id)] = res
        })
    },

    cancelEdit(id) {
      this.editing = this.editing.filter(ed => ed !== id);
    },

    addEdit(id) {
      this.editing.push(id)
    },

    moveToDelete(id) {
      this.deleted.push(this.humans.find(human => human.id === id));
      this.humans = this.humans.filter(human => human.id !== id);
      this.cancelEdit(id)
    },

    checkMarried(human) {
      return this.married.length === 0 ? true : this.married === human.is_married;
    },

    checkSex(human) {
      return this.sex.length === 0 ? true : this.sex.includes(human.sex);
    },

    filteredHumans() {
      return this.humans.filter(human => this.checkMarried(human) && this.checkSex(human));
    }
  },
}
</script>
