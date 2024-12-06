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
    path('api/categories/', CategoryListView.as_view(), name='category-list'),          # Главная страница с категориями
    path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  # Страница конкретной категории с курсами
    path('api/knowledge/', NewKnowlegeView.as_view(), name='knowledge'),
    path('api/regestration/',RegestrationAPIView.as_view(), name='regestration'),

]

