from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    exist = models.BooleanField(default=False)
    specifies = models.TextField()
    reviews = models.TextField()
    additional_information = models.TextField()
    link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=50)
    search_history = models.TextField()
