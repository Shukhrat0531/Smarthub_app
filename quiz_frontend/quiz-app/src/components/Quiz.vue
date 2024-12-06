<template>
  <div class="bg-yellow-300 text-black p-4  mt-0 pt-20">
    <h1 class="text-center ">Вопросы</h1>
   
  
 <div class="top-80">
  <form @submit.prevent="submitQuiz">
    <ol type="1">
      <li v-for="(question, index) in questions" :key="question.id" class="mt-4">
        {{ question.id }}. {{ question.text }}
        <div v-for="choice in question.choices" :key="choice.id">
          <label>
            <input type="radio" :name="'question-' + question.id" :value="choice.id" v-model="answers[index]" />
            {{ choice.text }}
          </label>
        </div>
      </li>
    </ol>
 <div class="flex justify-center mt-10"> <!-- Центрирование кнопки -->
      <button class="w-40 rounded-3xl text-black bg-amber-400 h-14" type="submit">Закончить</button>
    </div>  </form>
  <div v-if="result">
    <h2>Your Score: {{ result.score }}/{{ result.total }}</h2>
  </div>
</div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questions: [],
      answers: [],
      result: null,
    };
  },
  created() {
    this.fetchQuestions();
  },
  methods: {
    fetchQuestions() {
  axios.get('http://localhost:8000/api/quiz/') // Убедитесь, что здесь правильный URL
    .then(response => {
      this.questions = response.data;
      this.answers = new Array(this.questions.length).fill(null);
    })
    .catch(error => {
      console.error(error);
    });
},

   submitQuiz() {
  const payload = {
    answers: this.answers.map((choice_id, index) => ({
      question_id: this.questions[index].id,
      choice_id: choice_id,
    })),
  };

  axios.post('http://localhost:8000/api/quiz/', payload)
    .then(response => {
      // Перенаправляем на страницу результатов с данными
      this.$router.push({ 
        path: '/result', 
        query: { score: response.data.score, total: response.data.total } 
      });
    })
    .catch(error => {
      console.error(error);
    });
}
  },
};
</script>
