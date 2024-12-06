<template>
    <div class="pt-20 bg-black text-yellow-400 min-h-screen">
        <Header></Header>
        <div class="container mx-auto px-6 py-10">
            <h1 class="text-4xl font-bold text-center mb-8">Hello Page</h1>
            <div v-if="category" class="bg-yellow-100 text-black p-6 rounded-lg shadow-lg">
                <h1 class="text-3xl font-semibold mb-4">{{ category.name }}</h1>
                <p class="text-lg mb-4">{{ category.title }}</p>
                <img :src="`http://localhost:8000/${category.img}`"  alt="Category Image" class="w-full h-auto rounded-lg mb-6" />

                <!-- Курсы -->
                <div 
                    v-for="course in category.courses" 
                    :key="course.id" 
                    class="course bg-black text-yellow-400 border border-yellow-400 p-4 rounded-lg mb-6 shadow-md"
                >
                    <h2 class="text-2xl font-semibold mb-2">{{ course.name }}</h2>
                    <p class="text-lg mb-4">{{ course.description }}</p>
                    <img :src="`http://localhost:8000/${course.img}`" alt="Course Image" class="w-full h-auto rounded-lg mb-4" />
                    <p class="mb-2"><span class="font-semibold">About Course:</span> {{ course.about_course }}</p>
                    <p class="mb-4"><span class="font-semibold">Price:</span> {{ course.price }}</p>
                    <div class="flex space-x-4">
                        <img 
                            v-if="course.img2" 
                            :src="`http://localhost:8000/${course.img2}`" 
                            alt="Additional Image 1" 
                           @error="hideImage($event)" 
                            class="w-1/2 h-auto rounded-lg"
                        />
                        <img 
                         v-if="course.img3" 
                             :src="`http://localhost:8000/${course.img3}`" 
                            alt="Additional Image 2" 
                           
                            class="w-1/2 h-auto rounded-lg"
                        />
                    </div>
                    <p class="mt-4"><span class="font-semibold">Extra Fields:</span> {{ course.extra_feildes }}</p>
                </div>
            </div>
        </div>
        <Block></Block>
    </div>
</template>

<script>
import Header from '../components/Header.vue';
import Block from '@/components/Block.vue';
export default {
    components: {
        Header,
        Block,
    },
    props:['id'],
    data(){
        return {
            category:null,
        }
    },
    methods:{
       async fetchCategoryDetail() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/categories/${this.id}/`);
            this.category = await response.json();
            console.log(this.category);
        } catch (error) {
            console.log(error);
        }
    },
        
    },
    mounted() {
        this.fetchCategoryDetail();
    },
};
</script>
<style>
</style>

