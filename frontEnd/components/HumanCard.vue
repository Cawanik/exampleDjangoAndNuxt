<template>
  <v-card class="v-card v-card--flat">
      <h5 class="v-card__title">{{ human.first_name }}</h5>
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
        <strong>Role:</strong> {{ human.role_id }}
      </v-card-text>
      <v-card-actions class="action-buttons">
        <v-btn @click="onEdit(human.id)" class="v-btn">Edit</v-btn>
        <v-btn @click="onDelete(human.id)" class="v-btn">Delete</v-btn>
      </v-card-actions>
  </v-card>
</template>

<script>
//todo Привести верстку в порядок, 1) С директивами vuetify.js, 2) Собрать кастомный css внутри папки assets, 3) Вынести edit/add в модальные окна, не делать view, 4) В формах сделать валидацию, 5) Сделать валидацию на бэке, 6) Разделить список humans на 3 списка мужчина, женатые, женщина, если у мужчины или женщины возраст больше 40, сделать красную индекацию в углу карточки, 7) Вычистить ненужный хлам из проекта, 8) Сделать связь с ролями
export default {
  name: "HumanCard",
  props: ["human", "onDelete", "onEdit"]
};
</script>


