from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class Ticher(models.Model):
    name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    about_tich=models.TextField()
    phone= models.IntegerField(max_length=12)
    image = models.ImageField(upload_to='upload',blank=True,null=True)
    professions = models.CharField(max_length=20)
    professions = models.ManyToManyField('Lesson') 
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class OrderLesson(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Отработан'),
        ('not_completed', 'Не отработан'),
        ('contacted', 'Поднял трубку'),
        ('not_contacted', 'Не поднял трубку'),
    ]
    name_students = models.CharField(max_length=30)
    phone_students = models.IntegerField(max_length=12)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='lesson')  
    ticher = models.ForeignKey(Ticher,on_delete=models.CASCADE)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_completed')

    
    def __str__(self):
        return self.name_students
    