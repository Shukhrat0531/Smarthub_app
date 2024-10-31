<template>
    <div class="relative h-screen">
        <div class="absolute inset-0 flex items-center justify-center w-full">
            <div class="flex flex-col items-center justify-center z-20">
                <h1 class="text-6xl text-white font-extrabold text-center">SMART HUB</h1>
                <p class="text-white">Lorem ipsum dollar</p>
                <button class="border-yellow-300 border text-yellow-300 w-40 h-10 rounded-lg mt-5 bg-transparent">УЗНАТЬ О НАС</button>
            </div>
        </div>
        <div class="absolute inset-0">
            <video class="filter brightness-50 w-full h-full object-cover" autoplay loop muted>
                <source :src="Vidieosrc" type="video/mp4">
                Ваш браузер не поддерживает видео.
            </video>
        </div>
    </div>
</template>

<script>
import myVideo from "@/assets/5427891-uhd_3840_2160_25fps.mp4";

export default {
    data() {
        return {
            Vidieosrc: myVideo,
        };
    },
};
</script>

<style scoped>
</style>
