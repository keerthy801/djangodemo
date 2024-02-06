from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    image=models.ImageField(upload_to="designapp/image",null=True,blank=True)

    def __str__(self):
        return self.name

class team(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    image=models.ImageField(upload_to="designapp/team",null=True,blank=True)

    def __str__(self):
        return self.name