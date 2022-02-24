from django.contrib.auth import get_user_model
from django.db import models

from applications.author.models import Author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    title = models.CharField(max_length=100)
    date_of_publish = models.DateTimeField(auto_now=False)
    picture = models.ImageField(upload_to='media')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_bestseller = models.BooleanField(blank=True)

    def __str__(self):
        return self.title
