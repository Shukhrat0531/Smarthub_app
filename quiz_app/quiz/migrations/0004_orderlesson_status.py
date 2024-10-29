# Generated by Django 5.0.4 on 2024-10-25 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_lessoon_orderlesson_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlesson',
            name='status',
            field=models.CharField(choices=[('completed', 'Отработан'), ('not_completed', 'Не отработан'), ('contacted', 'Поднял трубку'), ('not_contacted', 'Не поднял трубку')], default='not_completed', max_length=20),
        ),
    ]