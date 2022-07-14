from pyexpat import model
from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=255, default='Asadbek')
    color = models.CharField(max_length=255, default='red')
    age = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self .name


    def desc(self):
        return self.description[:50]
    


