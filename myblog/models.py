from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=250)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
