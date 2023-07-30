import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Attributes: question_text and pub_date"""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= \
            self.pub_date <= now

    def get_absolute_url(self):
        return reverse('polling_question_detail',
                       kwargs={'pk': self.pk})

    def get_vote_url(self):
        return reverse('polling_question_vote',
                       kwargs={'pk': self.pk})


class Choice(models.Model):
    """Attributes: question, choice_text and votes"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
