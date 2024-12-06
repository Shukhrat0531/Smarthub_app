
# Сериализаторы для моделей
from rest_framework import serializers
from .models import *

# для регестрациии
from django.contrib.auth.models import User

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']


class OrderLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLesson
        fields = '__all__'
    

class TicherSerializer(serializers.ModelSerializer):
    professions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Ticher
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name']         

# Сериализатор курса
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# Сериализатор для главной страницы: только категории
class CategoryCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCourse
        fields = ['id', 'name', 'img', 'title']  # Основные поля для категории

# Сериализатор для страницы категории с вложенными курсами
class CategoryCourseDetailSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = CategoryCourse
        fields = '__all__'
#Сериализатор для  что они получать 
class NewKnowlegeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewKnowlege
        fields = '__all__'
        
#REgestration
class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Валидация совпадения паролей
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    # Создание нового пользователя
    def create(self, validated_data):
        password = validated_data.pop('password1')  # Получаем пароль
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )
        user.save()
        return user