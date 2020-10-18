from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile_no = models.IntegerField(null=True)
    profile_image = models.FileField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, null=True)
    heigth = models.CharField(max_length=100, null=True)
    weight = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.first_name


class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Task_date = models.DateField(null=True)
    Due_date = models.DateField(null=True)
    task_name = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.task_name

class TaskCompleted(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   task_name = models.ForeignKey(Goals, on_delete=models.CASCADE)
   points = models.IntegerField(null=True)

class Food_details(models.Model):
    user = models.ForeignKey(User_details, on_delete=models.CASCADE, null=True)
    calories = models.CharField(max_length=100, null=True)
    food_type = models.CharField(max_length=500, null=True)
    calculate = models.IntegerField(null=True)

    def __str__(self):
        return self.food_type
