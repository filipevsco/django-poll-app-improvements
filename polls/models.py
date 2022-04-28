import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.TextField(max_length=1000, default="Only description")
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

    @admin.display(boolean=True, ordering='pub_date', description="Published recently?")
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text