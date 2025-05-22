from django.db import models


class Book(models.Model):
    position = models.IntegerField()


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
