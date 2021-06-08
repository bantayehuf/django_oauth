from django.db import models


class Student(models.Model):
    name = models.CharField('Student name' ,max_length=50)