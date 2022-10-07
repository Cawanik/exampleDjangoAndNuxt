<template>
  <div class="card recipe-card">
    <div class="card-body">
      <h5 class="card-title">{{ human.first_name }}</h5>
      <p class="card-text">
        <strong>Last name:</strong> {{ human.last_name }}
      </p>
      <p class="card-text">
        <strong>Patronymic:</strong> {{ human.patronymic }}
      </p>
      <p class="card-text">
        <strong>Age:</strong> {{ human.age }}
      </p>
      <p class="card-text">
        <strong>Sex:</strong> {{ human.sex }}
      </p>
      <p class="card-text">
        <strong>Is married:</strong> {{ human.is_married }}
      </p>
      <p class="card-text">
        <strong>Role:</strong> {{ human.role_id }}
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/humans/${human.id}/`" class="btn btn-sm btn-success">View</nuxt-link>
        <nuxt-link :to="`/humans/${human.id}/edit/`" class="btn btn-sm btn-primary">Edit</nuxt-link>
        <button @click="onDelete(human.id)" class="btn btn-sm btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
//todo Привести верстку в порядок, 1) С директивами vuetify.js, 2) Собрать кастомный css внутри папки assets, 3) Вынести edit/add в модальные окна, не делать view, 4) В формах сделать валидацию, 5) Сделать валидацию на бэке, 6) Разделить список humans на 3 списка мужчина, женатые, женщина, если у мужчины или женщины возраст больше 40, сделать красную индекацию в углу карточки, 7) Вычистить ненужный хлам из проекта, 8) Сделать связь с ролями
export default {
  name: "HumanCard",
  props: ["human", "onDelete"]
};
</script>

<style>
.recipe-card {
  box-shadow: 0 1rem 1.5rem rgba(0, 0, 0, .6);
}
</style>


