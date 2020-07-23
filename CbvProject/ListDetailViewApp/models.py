from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    Principal = models.CharField(max_length=256)
    Location = models.CharField(max_length=256)
    def __str__(self):
        return self.name
    def get_absolute_url(self):     # after creating a view,goes to detail page
        return reverse("ListDetailViewApp:list")

class Students(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    def __str__(self):
        return self.name