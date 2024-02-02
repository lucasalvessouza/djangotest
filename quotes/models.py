from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)


class Quotes(models.Model):
    quote = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, name='author_id')

