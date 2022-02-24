from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False)
    place_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return self.name
