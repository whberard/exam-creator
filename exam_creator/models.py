from django.db import models


# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    book_section = models.CharField(max_length=100)

    def __str__(self):
        return u'%s, %s' %(self.book_section, self.topic_name)

class Question(models.Model):
    latex = models.TextField()
    source = models.CharField(max_length=100)
    notes = models.TextField()
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        # Return the first five words of a question to display it.
        first_words = self.latex.split()[:5]
        first_words = " ".join(first_words)
        return first_words


