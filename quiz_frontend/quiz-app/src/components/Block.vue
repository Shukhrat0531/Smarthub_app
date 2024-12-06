<template>
  <div class="max-w-4xl mx-auto text-center mt-10 px-4">
    <h2 class="text-3xl font-bold text-white mb-6">ЧЕМУ НАУЧИТЕСЬ</h2>
    <div 
      v-for="block in blocks" 
      :key="block.id"
      class="rounded-lg p-8 mb-6 shadow-md text-left relative bg-cover bg-center bg-no-repeat"
      :style="{ backgroundImage: `url(http://localhost:8000/${block.img})` }" 
    >
      <!-- Полупрозрачный слой поверх фона -->
      <div class="absolute inset-0 bg-black bg-opacity-50 rounded-lg"></div>
      
      <!-- Основное содержимое -->
      <div class="relative z-10">
        <h3 class="text-xl font-semibold mb-4 text-white">{{ block.title }}</h3>
        <p class="text-base text-white">{{ block.description }}</p>
      </div>
      
      <!-- Второе фото в правом углу -->
      <img 
        :src="`http://localhost:8000/${block.emodje}`" 
        alt="Дополнительное изображение" 
        class="absolute top-4 right-4 w-12 h-12 object-contain z-20"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      blocks: []
    };
  },
  created() {
    this.fetchBlockInfo();
  },
  methods: {
    fetchBlockInfo() {
      axios.get('http://localhost:8000/api/knowledge/')
        .then(response => {
          this.blocks = response.data;
          console.log(this.blocks);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
/* Если нужно добавить дополнительные стили */
</style>
