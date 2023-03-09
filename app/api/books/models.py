from django.db import models

class Book(models.Model):
  name = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  year = models.IntegerField(max_length=4)
  pages = models.IntegerField(max_length=4)
  description = models.CharField(max_length=1000)
  class Meta:
    db_table = 'books'
