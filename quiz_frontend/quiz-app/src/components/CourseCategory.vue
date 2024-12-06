<template>
  <swiper
    :slidesPerView="4"
    :spaceBetween="0"
    :pagination="{ clickable: true }"
    :modules="modules"
    class="mySwiper"
  >
  <swiper-slide 
    v-for="category in categories" 
    :key="category.id"
    @click="goToCategoryDetails(category.id)"
    >
      <div to="" class=" w-full relative bg-slate-800 h-48 flex flex-col justify-center items-center overflow-hidden">
        <!-- Добавляем фон с затемнением и эффектом зума при наведении -->
        <div
          :style="{ backgroundImage: `url(http://localhost:8000/${category.img})` }"
          class="bg-image h-full cursor-pointer transition-transform transform hover:scale-105"
        >
          <div class="overlay flex flex-col justify-center items-center h-full w-full">
            <h2 class="text-white font-bold text-lg">{{ category.name }}</h2>
            <p class="text-white">{{ category.title }}</p>
          </div>
        </div>
      </div>
    </swiper-slide>
  </swiper>
</template>


<script>
  // Import Swiper Vue.js components
  import { Swiper, SwiperSlide } from 'swiper/vue';

  // Import Swiper styles
  import 'swiper/css';

  import 'swiper/css/pagination';

  import '../assets/style.css';

  import { RouterLink, RouterView } from 'vue-router'

  // import required modules
  import { Pagination } from 'swiper/modules';

  export default {
    data(){
      return {
        categories:[],
      };
    },
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [Pagination],
      };
    },
    mounted() {
      this.fetchCategory();
    },
    methods: {
      async fetchCategory(){
        try{
          const response = await fetch('http://127.0.0.1:8000/api/categories/');
          const data = await response.json();
          this.categories = data;
          console.log(data);
        }catch(error){
          
          console.error('Error fetching categories', error);
        }
      },
      goToCategoryDetails(id){
        // Вызываем функцию для перехода на страницу категории
        this.$router.push({ name: 'category_detail', params: { id } });
      },
    },
  };
</script>
<style>
.bg-image {
  background-size: cover;
  background-position: center;
  transition: transform 0.3s ease; /* Плавный переход */
  position: relative;
}

/* Полупрозрачное наложение для затемнения */
.overlay {
  background-color: rgba(0, 0, 0, 0.5); /* Полупрозрачный черный цвет */

  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  transition: background-color 0.3s ease;
}

/* Эффекты при наведении */
.bg-image:hover .overlay {
  background-color: rgba(0, 0, 0, 0); /* Убираем затемнение */
}

.bg-image:hover {
  transform: scale(1.05); /* Увеличение при наведении */
}
</style>