from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):
    sc_name=models.CharField(max_length=10)
    sc_princi=models.CharField(max_length=10)
    sc_loc=models.CharField(max_length=10)

    def __str__(self):
        return self.sc_name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


class Student(models.Model):
    sname=models.CharField(max_length=10)
    sage=models.IntegerField()
    sc_name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='panda')

    def __str__(self):
        return self.sname