<template>
  <div class="m-auto">
    <br><br>
    <h2 class="text-center">Ваш балл: {{ score }}/{{ total }}</h2>
    <div v-if="score >= 1">
      <p class="text-center">Поздравляем! <br>Ваш уровен равен <span class="bg-green-500 text-white">Pre-intermadite</span>!</p>
    </div>
    <div v-else>
      <p>Вам надо начать с алфавита </p>
    </div><br>
    <router-link class="text-blue-500 text-center" to="/">Вернуться к главной страницу</router-link>
  </div>
</template>
<script>
export default {
  computed: {
    score() {
      return parseInt(this.$route.query.score); // Преобразуем в целое число
    },
    total() {
      return this.$route.query.total;
    },
  },
};
</script>
