<template>
  <v-card class="v-card v-card--flat">
    <v-text-field
      v-model="human.first_name"
      label="First name*"
      required
    />
    <v-text-field
      v-model="human.last_name"
      label="Last name*"
      required
    />
    <v-text-field
      v-model="human.patronymic"
      label="Patronymic"
      required
    />
    <v-text-field
      v-model="human.age"
      label="Age*"
      type="number"
      required
    />
    <v-text-field
      v-model="human.email"
      label="E-mail*"
      type="email"
      required
    />
    <v-text-field
      v-model="human.password"
      label="Password*"
      type="password"
      required
    />
    <v-select
      v-model="human.sex"
      :items="selectItemsSex"
      label="Sex*"
      required
    />
    <v-select
      label="Status*"
      v-model="human.is_married"
      :items="selectItemsMarried"
      item-text="name"
      item-value="value"
      required
    />
    <v-select
      v-model="roleId"
      :items="roles"
      item-text="name"
      item-value="id"
      label="Role*"
    />
    <v-card-actions class="action-buttons">
      <v-btn @click="cancelEdit()" class="v-btn">Cancel</v-btn>
      <v-btn @click="onSubmit()" class="v-btn" color="green">Submit</v-btn>
      <v-btn @click="onDelete()" class="v-btn" color="red">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "HumanEditingCard",
  props: {
    human: {
      type: Object,
      required: true
    },
    roles: {
      type: Array,
      required: true
    }
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
      roleId: 0,
    };
  },
  methods: {
    onDelete() {
      this.$axios.$delete(`/humans/${this.human.id}/`)
        .then(res => {
          this.$parent.humans = this.$parent.humans.filter(el => {
            return el.id !== this.human.id;
          })
        })
        .catch(err => {
          this.$nuxt.error({statusCode: err.response.status, message: err.response.statusText})
        })
    },
    cancelEdit() {
      this.$parent.editing = this.$parent.editing.filter(el => {
        return el !== this.human.id;
      })
    },
    onSubmit() {
      this.cancelEdit();
      if (this.roleId) {
        this.human.role = this.roleId;
      } else {
        this.human.role = this.roles.find(el => el.name === this.human.role).id;
      }

      this.$axios.$patch(`/humans/${this.human.id}/`, this.human)
        .then(res => {
          let indexEditingElement = this.$parent.humans.indexOf(this.$parent.humans.find(el => {
            return el.id === res.id;
          }));
          this.$parent.humans.splice(indexEditingElement, 1, res)
        })
        .catch(err => {
          this.$nuxt.error({statusCode: err.response.status, message: err.response.statusText})
        })
    },
  }
}

</script>
