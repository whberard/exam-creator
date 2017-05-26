from django.db import models


class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    book_section = models.CharField(max_length=100)

# Create your models here.
class Question(models.Model):
    latex = models.TextField()
    source = models.CharField(max_length=100)
    notes = models.TextField()
    topics = models.ManyToManyField(Topic)


