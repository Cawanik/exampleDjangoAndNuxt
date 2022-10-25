<template>
  <v-dialog max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="text--black" v-bind="attrs" v-on="on">
        Add human
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Human Characteristic</span>
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              :error-messages="errors.first_name"
              v-model="human.first_name"
              label="First name*"
              required>
            </v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              :error-messages="errors.last_name"
              v-model="human.last_name"
              label="Last name*"
              required/>
          </v-col>
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              :error-messages="errors.patronymic"
              v-model="human.patronymic"
              label="Patronymic"
              hint="if no patronymic stay empty"
              persistent-hint/>
          </v-col>
          <v-col cols="12" sm="6">
            <v-select
              :error-messages="errors.sex"
              v-model="human.sex"
              :items="selectItemsSex"
              label="Sex*"
              required
            />
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              :error-messages="errors.age"
              v-model="human.age"
              label="Age*"
              type="number"
              required
            />
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              :error-messages="errors.email"
              v-model="human.email"
              label="E-mail*"
              type="email"
              required
            />
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              :error-messages="errors.password"
              v-model="human.password"
              label="Password*"
              type="password"
              required
            />
          </v-col>
          <v-col cols="12" sm="6">
            <v-select
              label="Status*"
              :error-messages="errors.is_married"
              v-model="human.is_married"
              :items="selectItemsMarried"
              item-text="name"
              item-value="value"
              required
            />
          </v-col>
          <v-col cols="12" sm="6">
            <v-select
              v-model="human.role"
              :items="$parent.roles"
              item-text="name"
              item-value="id"
              label="Role*"
            />
          </v-col>
        </v-row>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="white darken-1" text @click="addHuman()">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "HumanAddDialog",
  props: {
    roles:{
      type: Array,
      required: true
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
        role: 0,
        email: 'cawa@cawa.cawa',
        password: ''
      },
      selectItemsMarried: [
        {name: 'Is married', value: true},
        {name: 'Is not married', value: false}
      ],
      selectItemsSex: [
        'Women',
        'Men',
        'Middle'
      ],
      errors: {}
    };
  },
  methods: {
    addHuman() {
      this.errors = {};
      this.$axios.$post(`/humans/`, this.human)
        .then(res => {
          this.human = res;
          this.$emit('add', this.human);
        })
        .catch(err => {
          this.errors = err.response.data[0];
        })
    },
  }
}
</script>
