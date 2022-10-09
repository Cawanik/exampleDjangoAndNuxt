<template>
  <v-card class="v-card v-card--flat">
    <v-container>
      <v-row>
        <h5 class="v-card__title">{{ human.first_name }}</h5>
        <v-icon v-if="ageCheck" color="red" right>mdi-alert-circle</v-icon>
      </v-row>
    </v-container>
    <v-card-text class="v-card__text">
      <strong>Last name:</strong> {{ human.last_name }}
    </v-card-text>
    <v-card-text class="v-card__text">
      <strong>Patronymic:</strong> {{ human.patronymic }}
    </v-card-text>
    <v-card-text class="v-card__text">
      <strong>Age:</strong> {{ human.age }}
    </v-card-text>
    <v-card-text class="v-card__text">
      <strong>Sex:</strong> {{ human.sex }}
    </v-card-text>
    <v-card-text class="v-card__text">
      <strong>Is married:</strong> {{ human.is_married }}
    </v-card-text>
    <v-card-text class="v-card__text">
      <strong>Role:</strong> {{ humanRoleName }}
    </v-card-text>
    <v-card-actions class="action-buttons">
      <v-btn @click="onEdit(human.id)" color="blue" class="v-btn">Edit</v-btn>
      <v-btn @click="onDelete(human.id)" color="red" class="v-btn">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
//todo 2) Собрать кастомный css внутри папки assets, 4) В формах сделать валидацию, 5) Сделать валидацию на бэке
export default {
  name: "HumanCard",
  props: ["human", "roles", "onDelete", "onEdit"],
  computed: {
    humanRoleName() {
      return this.roles.find(role => {
        return role.id === this.human.role_id;
      }).name;
    },
    ageCheck() {
      return this.human.age > 40
    }
  }
};
</script>


