# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.quiz_view, name='quiz'),
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('api/quiz/', QuizAPIView.as_view(), name='quiz-api'),
    path('api/tichers/', TicherSerializerByLesson.as_view(), name='ticher-list-by-lesson'),
    path('api/orders/', CreateOrderLessons.as_view(), name='create-order'),
    path('api/lessons/', LessonListAPIView.as_view(), name='lesson-list'),

]

