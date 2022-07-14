from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=255,default='Asadbek')
    age = models.IntegerField()
    city = models.CharField(max_length=255,default='Uzbekistan')
    date = models.DateField()
    description = models.TextField()
    images = models.ImageField(upload_to='backend_images', blank='true')


    def __str__(self):
        return self.name

    def desc(self):
        return self.description[:50]



class MainId(models.Model):
    main_id = models.ForeignKey(Main, on_delete=models.CASCADE,related_name='related_name')
    gender = models.CharField(max_length=100)


    def __str__(self):
        return self.gender