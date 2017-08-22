from django.db import models

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name