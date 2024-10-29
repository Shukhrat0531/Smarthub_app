# from django.shortcuts import render, redirect
# from .models import Question, Choice

# def quiz_view(request):
#     questions = Question.objects.all()

#     if request.method == 'POST':
#         score = 0
#         for question in questions:
#             selected_choice = request.POST.get(str(question.id))
#             if selected_choice:
#                 choice = Choice.objects.get(id=selected_choice)
#                 if choice.is_correct:
#                     score += 1

#         return render(request, 'quiz/result.html', {'score': score, 'total': questions.count()})

#     return render(request, 'quiz/quiz.html', {'questions': questions})


# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

class QuizAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        score = 0
        for answer in request.data.get('answers', []):
            try:
                choice = Choice.objects.get(id=answer['choice_id'])
                if choice.is_correct:
                    score += 1
            except Choice.DoesNotExist:
                continue
        
        total = Question.objects.count()
        return Response({'score': score, 'total': total}, status=status.HTTP_200_OK)


class CreateOrderLessons(APIView):
    def post(self, request):
        serializer = OrderLessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicherSerializerByLesson(APIView):
    def get(self, request):
        lesson_id = request.query_params.get('lesson_id')  # Получаем lesson_id из параметров запроса
        if lesson_id:
            tichers = Ticher.objects.filter(professions__id=lesson_id)
        else:
            tichers = Ticher.objects.all()  # Если нет lesson_id, вернуть всех учителей
        
        serializer = TicherSerializer(tichers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LessonListAPIView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)