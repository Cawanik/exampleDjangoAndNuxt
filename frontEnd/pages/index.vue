<template>
  <header>
    <div class="text-box">
      <h1>Всем хай</h1>
      <p class="mt-3">Список долбоебов</p>
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/humans">
        Посмотреть долбоебов
      </nuxt-link>
    </div>
  </header>
</template>

<script>
export default {
  head() {
    return {
      title: "Домашняя страница"
    };
  },
};
</script>

<style>
header {
  min-height: 100vh;
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-family: cursive;
  font-size: 5rem;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
