# serializers.py
from rest_framework import serializers
from .models import *

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