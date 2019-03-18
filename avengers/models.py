from django.db import models


class Avenger(models.Model):
    avenger_name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    add_date = models.DateTimeField(auto_now_add=True)

    referrals = models.IntegerField(default=0)

    def create(self):
        self.save()

    def __str__(self):
        return self.avenger_name
