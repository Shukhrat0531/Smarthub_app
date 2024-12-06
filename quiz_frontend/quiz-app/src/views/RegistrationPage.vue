<template>
  <div class="pt-16 bg-yellow-100 h-screen">
    <form @submit.prevent="RegisterUser" class="mx-auto w-80 p-4 border border-gray-300 rounded-lg shadow-md">
      <div class="mb-4">
        <label for="name" class="block text-gray-700 font-medium mb-2">
          Имя
        </label>
        <input 
          type="text" 
          id="name" 
          v-model="form.username"
          class="w-full h-10 px-3 border border-yellow-400 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400"
          placeholder="Введите ваше имя"
        />
      </div>

      <div class="mb-4  ">
        <label for="phone" class="block text-gray-700 font-medium mb-2">
          Email
        </label>
        <input 
          type="tel" 
          id="email" 
          v-model="form.email"
          class="w-full h-10 px-3 border border-yellow-400 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400"
          placeholder="Введите номер телефона"
        />
      </div>

      <div class="mb-4">
        <label for="password" class="block text-gray-700 font-medium mb-2">
          Пароль
        </label>
        <input 
          type="password" 
          id="password1" 
          v-model="form.password1" 
          class="w-full h-10 px-3 border border-yellow-400 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400"
          placeholder="Введите пароль"
        />
      </div>

      <div class="mb-4">
        <label for="password" class="block text-gray-700 font-medium mb-2">
          Повторите Пароль
        </label>
        <input 
          type="password" 
          id="password2" 
          v-model="form.password2"
          class="w-full h-10 px-3 border border-yellow-400 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400"
          placeholder="Введите пароль еще раз"
        />
      </div>

      <button 
        type="submit"
        class="w-full h-10 bg-yellow-400 text-white font-medium rounded-md hover:bg-yellow-500 focus:outline-none focus:ring-2 focus:ring-yellow-400"
      >
        Зарегистрироваться
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
 
  name: "RegistrationForm",
  data() {
    return {
      form: {
        username: "",
        email: "",
        password1: "",
        password2: ""
      }
    };
  },
  methods: {
    async RegisterUser(){
        try {
            const response = await axios.post('http://localhost:8000/api/regestration/', this.form);
            console.log(response);
            //  this.$toast.success("Регистрация успешна!");

      // Перенаправление на главную страницу
            this.$router.push('/');
        }catch(error){
            console.error(error);
            // this.$toast.error("Ошибка при регистрации");
        }
    }
  }
};
</script>

<style>

</style>

