from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  class Meta:
    db_table = 'user_profile'

class UserBooks(models.Model):
  profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  class Meta:
    db_table = 'user_books'