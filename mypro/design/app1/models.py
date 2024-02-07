from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='image/place',null=True,blank=True)
    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to='image/Team',null=True,blank=True)
    def __str__(self):
        return self.name