<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
</script>

<template>
  <div>
   <!-- <header class="bg-yellow-400  py-4 shadow-md fixed w-full z-40">
  <div class="wrapper max-w-7xl mx-auto px-6">
    <nav class="flex items-center justify-between">
      <div class="text-lg font-semibold">
        <RouterLink to="/" class="hover:text-blue-300">SH</RouterLink>
      </div>
      <div class="space-x-6">
        <RouterLink to="/" class="hover:text-red-900 transition duration-200">Сдать тест</RouterLink>
        <RouterLink to="/about" class="hover:text-red-900 transition duration-200">Оставить заявку </RouterLink>
      </div>
    </nav>
  </div>
</header> -->

<Header></Header>
  <RouterView />
  </div>
</template>

<style scoped>

</style>

<!-- 

 -->