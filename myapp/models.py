from django.db import models
class Color(models.Model):
    color_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name

class Person(models.Model):
    name = models.CharField(max_length=120)
    age  = models.IntegerField()
    color2 = models.ForeignKey(Color, on_delete=models.CASCADE,related_name="color")
    def __str__(self):
        return self.name
