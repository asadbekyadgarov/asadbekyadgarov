from itertools import count
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.urls import reverse


class Main(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    qarz = models.IntegerField(default=0)
    img = models.ImageField(upload_to='backend_images', blank='true')

    def __str__(self):
        return self.name

class Tovar(models.Model):
    main_id = models.ForeignKey(Main, on_delete=models.CASCADE)
    tovar_nomi = models.CharField(max_length=255)
    count = models.IntegerField()
    price = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('main', kwargs={'raqam': self.slug})



class Payment(models.Model):
    pay = models.IntegerField()
    main_foreign_key = models.ForeignKey(Tovar,on_delete=models.CASCADE)


