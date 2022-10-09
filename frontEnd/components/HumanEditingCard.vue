<template>
  <v-card class="v-card v-card--flat">
    <v-col cols="12">
      <v-text-field
        v-model="human.first_name"
        label="First name*"
        required
      />
    </v-col>
    <v-col cols="12">
      <v-text-field
        v-model="human.last_name"
        label="Last name*"
        required
      />
    </v-col>
    <v-col cols="12">
      <v-text-field
        v-model="human.patronymic"
        label="Patronymic"
        required
      />
    </v-col>
    <v-col>
    <v-text-field
                v-model="human.age"
                label="Age*"
                type="number"
                required
              />
    </v-col>
    <v-col cols="12">
      <v-select
        v-model="human.sex"
        :items="['Men', 'Women', 'Middle', 'None']"
        label="Sex*"
        required
      />
    </v-col>
    <v-col cols="12">
      <v-select
                label="Status*"
                v-model="human.is_married"
                :items="[{name:'Is married', value: true}, {name:'Is not married', value: false}]"
                item-text="name"
                item-value="value"
                required
              />
    </v-col>
    <v-col cols="12">
      <v-select
                v-model="human.role_id"
                :items="roles"
                item-text="name"
                item-value="id"
                label="Role*"
              />
    </v-col>
    <v-card-actions class="action-buttons">
      <v-btn @click="onCancel(human.id)" class="v-btn">Cancel</v-btn>
      <v-btn @click="onSubmit(human)" class="v-btn" color="green">Submit</v-btn>
      <v-btn @click="onDelete(human.id)" class="v-btn" color="red">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "HumanEditingCard",
  props: ["human", "roles", "onDelete", "onSubmit", "onCancel"]
}
</script>

<style scoped>

</style>
