<template>
  <v-card class="v-card v-card--flat">
    <v-text-field
      v-model="human.first_name"
      label="First name*"
      :error-messages="errors.first_name"
      required
    />
    <v-text-field
      v-model="human.last_name"
      :error-messages="errors.last_name"
      label="Last name*"
      required
    />
    <v-text-field
      v-model="human.patronymic"
      :error-messages="errors.patronymic"
      label="Patronymic"
      required
    />
    <v-text-field
      v-model="human.age"
      :error-messages="errors.age"
      label="Age*"
      type="number"
      required
    />
    <v-text-field
      v-model="human.email"
      :error-messages="errors.email"
      label="E-mail*"
      type="email"
      required
    />
    <v-text-field
      v-model="human.password"
      :error-messages="errors.password"
      label="Password*"
      type="password"
      required
    />
    <v-select
      v-model="human.sex"
      :error-messages="errors.sex"
      :items="selectItemsSex"
      label="Sex*"
      required
    />
    <v-select
      v-model="human.is_married"
      :error-messages="errors.is_married"
      :items="selectItemsMarried"
      item-text="name"
      item-value="value"
      label="Status*"
      required
    />
    <v-select
      v-model="roleId"
      :error-messages="errors.roles"
      :items="roles"
      item-text="name"
      item-value="id"
      label="Role*"
    />
    <v-card-actions class="action-buttons">
      <v-btn @click="cancelEdit()">Cancel</v-btn>
      <v-btn @click="onSubmit()" color="green">Submit</v-btn>
      <v-btn @click="onDelete()" color="red">Delete</v-btn>
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

      errors:{},

      roleId: this.roles.find(el=>el.name=this.human.role).id,
    };
  },
  methods: {
    onDelete() {
      this.$axios.$delete(`/humans/${this.human.id}/`)
        .then(res => {
          this.$emit('delete');
        })
        .catch(err => {
          this.$nuxt.error({
            statusCode: err.response.status,
            message: err.response.data ? err.response.data : err.response.statusText
          })
        })
    },

    cancelEdit() {
      this.errors = {};
      this.$emit('cancel');
    },

    onSubmit() {
      this.errors = {};
      this.human.role = this.roleId
      this.$axios.$patch(`/humans/${this.human.id}/`, this.human)
        .then(res => {
          this.cancelEdit();
          this.$emit('submit');
        })
        .catch(err => {
          this.errors = err.response.data[0];
        })
    },
  }
}

</script>
