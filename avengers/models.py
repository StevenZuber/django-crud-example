from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Avenger(models.Model):

    avenger_name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    add_date = models.DateTimeField(auto_now_add=True)

    referrals = models.IntegerField(default=0)


    def __str__(self):
        return self.avenger_name

    def get_index_url(self):
        return ('avengers:index', [self.slug])

    def get_absolute_url(self):
        return ('avengers:index', [self.slug])

    def get_update_url(self):
        return ('avengers:update', [self.slug])

    def get_delete_url(self):
        return ('avengers:delete', [self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.avenger_name)
        super().save(*args, **kwargs)



