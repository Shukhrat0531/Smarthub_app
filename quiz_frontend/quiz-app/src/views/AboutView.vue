<script>
import axios from 'axios';
export default {
  data() {
    return {
      form: {
        name_student: '',
        phone_students: '',
        lesson: '',
        ticher: ''
      },
      lessons: [],
      tichers: [],
      selectLesson: null // Добавляем selectLesson
    }
  },
  async created() {
    await this.fetchLessons();
  },
  methods: {
    async fetchLessons() {
      try {
        const response = await axios.get('http://localhost:8000/api/lessons/');
        this.lessons = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchTicher() {
      if (this.selectLesson) {
        try {
          const response = await axios.get(`http://localhost:8000/api/tichers/?lesson_id=${this.selectLesson}`);
          this.tichers = response.data;
        } catch (error) {
          console.error(error);
        }
      }
    },
    submitOrder() {
      const payload = {
        name_students: this.form.name_student,
        phone_students: this.form.phone_students,
        lesson: this.selectLesson,
        ticher: this.form.ticher,
      };

      axios.post('http://localhost:8000/api/orders/', payload)
        .then(response => {
          alert('Заявка успешно отправлена!');
          // Очищаем форму
          this.form.name_student = '';
          this.form.phone_students = '';
          this.selectLesson = null;
          this.form.ticher = null;
        })
        .catch(error => {
          console.log('Отправка данных:', payload); 
          console.error('Ошибка при отправке заявки:', error);
        });
    },
  },
}
</script>

<template>
 <div class="about max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md mt-16">
  <form @submit.prevent="submitOrder" class="space-y-4">
    <div>
      <label for="name_students" class="block text-gray-700 font-medium mb-2">Имя Студента</label>
      <input
        type="text"
        v-model="form.name_student"
        required
        class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>

    <div>
      <label for="phone_students" class="block text-gray-700 font-medium mb-2">Телефон Студента</label>
      <input
        type="text"
        v-model="form.phone_students"
        required
        class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>

    <div>
      <label for="lesson" class="block text-gray-700 font-medium mb-2">Выберите предмет</label>
      <select
        v-model="selectLesson"
        @change="fetchTicher"
        required
        class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        <option v-for="lesson in lessons" :key="lesson.id" :value="lesson.id">
          {{ lesson.name }}
        </option>
      </select>
    </div>

    <div v-if="tichers.length">
      <label for="ticher" class="block text-gray-700 font-medium mb-2">Выберите учителя</label>
      <select
        v-model="form.ticher"
        required
        class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        <option v-for="ticher in tichers" :key="ticher.id" :value="ticher.id">
          {{ ticher.name }}
        </option>
      </select>
    </div>

    <button
      type="submit"
      class="w-full py-2 bg-yellow-500 text-white font-semibold rounded-md hover:bg-blue-600 transition duration-200"
    >
      Оставить заявку
    </button>
  </form>

  
</div>

</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
