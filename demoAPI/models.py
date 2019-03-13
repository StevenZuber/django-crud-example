from django.db import models

# Create your models here.

import datetime

from django.utils import timezone

class Avenger(models.Model):
    avenger_name = models.CharField(default='', max_length=50)

    add_date = models.DateTimeField('Date Added')

    referrals = models.IntegerField(default=0)

    def __str__(self):
        return self.avenger_name

