<template>
  <div class="relative">
    <!-- Кнопка для открытия меню -->
    <button @click="toggleMenu" class="  fixed top-1 h-10 left-1 right-1 z-50 bg-yellow-300 text-white px-4 py-2 rounded-md">
     <div v-if="!isMenuOpen" class="w-6 my_class  text-2xl">☰</div> 
    </button>
    
    <!-- Затемнение фона -->
    <div v-if="isMenuOpen" @click="toggleMenu" class="fixed inset-0 bg-black bg-opacity-50 z-40"></div>

    <!-- Боковое меню -->
    <div :class="{ 'translate-x-0': isMenuOpen, '-translate-x-full': !isMenuOpen }"
         class="fixed top-0 left-0 h-full w-4/5 max-w-xs bg-white z-50 transform transition-transform duration-300 ease-in-out shadow-lg">
      <button @click="toggleMenu" class="text-gray-500 text-lg p-4">
        Закрыть
      </button>
      <li class="tpnone px-4"><RouterLink to="/register" class="hover:text-red-900 transition duration-200">Регестрация</RouterLink></li>
      <ul class="mt-8 space-y-4 px-4">
        <li><RouterLink to="/" class="hover:text-red-900 transition duration-200">Главная</RouterLink></li>
        <li><RouterLink to="/about" class="hover:text-red-900 transition duration-200">Оставить заявку </RouterLink></li>
        <li><RouterLink to="/quiz" class="hover:text-red-900 transition duration-200">сдать тест </RouterLink></li>
        <li><a href="#" class="text-gray-700 hover:text-blue-500">Контакты</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'

export default {
  
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>
.my_class{
  margin-top:-5px;
}
.tpnone{
  list-style: none;
}
/* Убедитесь, что Tailwind подключен в вашем проекте */
</style>
