from django.contrib import admin
from .models import *
# from .models import User  # Импортируйте вашу кастомную модель User

# admin.site.register(User)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Ticher)
admin.site.register(Lesson)

class OrderLessonAdmin(admin.ModelAdmin):
    list_display = ('name_students', 'phone_students', 'lesson', 'ticher', 'status')
    list_filter = ('status', 'lesson', 'ticher')
    search_fields = ('name_students', 'phone_students')
    ordering = ('-id',)

admin.site.register(OrderLesson, OrderLessonAdmin)
admin.site.register(CategoryCourse)
admin.site.register(Course)
admin.site.register(NewKnowlege)
