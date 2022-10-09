<template>
  <v-dialog
    max-width="600px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="text--black"
        v-bind="attrs"
        v-on="on"
      >Add human</v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Human Characteristic</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col
              cols="12"
              sm="6"
              md="4"
            >
              <v-text-field
                v-model="human.first_name"
                label="First name*"
                required
              ></v-text-field>
            </v-col>
            <v-col
              cols="12"
              sm="6"
              md="4"
            >
              <v-text-field
                v-model="human.last_name"
                label="Last name*"
                required
              ></v-text-field>
            </v-col>
            <v-col
              cols="12"
              sm="6"
              md="4"
            >
              <v-text-field
                v-model="human.patronymic"
                label="Patronymic"
                hint="if no patronymic stay empty"
                persistent-hint
              ></v-text-field>
            </v-col>
            <v-col cols="12"
              sm="6">
              <v-select
                v-model="human.sex"
                :items="['Men', 'Women', 'Middle', 'None']"
                label="Sex*"
                required
              ></v-select>
            </v-col>
            <v-col cols="12"
              sm="6">
              <v-text-field
                v-model="human.age"
                label="Age*"
                type="number"
                required
              ></v-text-field>
            </v-col>
            <v-col
              cols="12"
              sm="6"
            >
              <v-select
                label="Status*"
                v-model="human.is_married"
                :items="[{name:'Is married', value: true}, {name:'Is not married', value: false}]"
                item-text="name"
                item-value="value"
                required
              ></v-select>
            </v-col>
            <v-col
              cols="12"
              sm="6"
            >
              <v-select
                v-model="human.role_id"
                :items="roles"
                item-text="name"
                item-value="id"
                label="Role*"
              ></v-select>
            </v-col>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="white darken-1"
          text
          @click="onAdd(human)"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "HumanAddDialog",
  props: ["roles", "onAdd"],
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
  }
}
</script>
