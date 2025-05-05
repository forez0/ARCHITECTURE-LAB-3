# domain/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order for {self.user} - {self.book}"
