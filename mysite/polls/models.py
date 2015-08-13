import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    """ Attributes for admin stuff """

    def __unicode__(self):
        return self.question_text

    def wasPublishedRecently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    wasPublishedRecently.admin_order_field = 'pub_date'
    wasPublishedRecently.boolean = True
    wasPublishedRecently.short_description = 'Publicado recientemente?'


class Choice(models.Model):

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.choice_text
