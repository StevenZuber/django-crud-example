from django.db import models

# Create your models here.
from django.urls import reverse


class Avenger(models.Model):

    avenger_name = models.CharField(max_length=50)

    add_date = models.DateTimeField(auto_now_add=True)

    referrals = models.IntegerField(default=0)


    def __str__(self):
        return self.avenger_name

    def get_absolute_url(self):
        return reverse('avengers:detail', kwargs={'pk': self.pk})