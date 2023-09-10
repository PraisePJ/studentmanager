from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=3)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    id_number = models.CharField(max_length=13)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=13)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    author = models.CharField(max_length=100, null=True)
    level = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class Result(models.Model):
    student_id = models.CharField(max_length=13, null=True)
    img = models.ImageField(upload_to='images/results', null=True)

    def __str__(self):
        return self.student_id
