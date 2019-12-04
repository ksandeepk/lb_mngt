from django.db import models
from django.urls import reverse

# Create your models here

class student(models.Model):
    reg_id=models.CharField(max_length=10)
    student_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    branch=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    

class book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='images/')
    Documents=models.FileField(upload_to='pdf/')
    branch=models.CharField(max_length=10)
    
    def get_absolute_url(self):
        return reverse('display_view')