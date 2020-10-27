from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class About_User(models.Model):
    USER_PROFILE_NUMBER = models.IntegerField(primary_key = True)
    USER_NAME= models.CharField(max_length = 20)
    USER_PHONE_NUMBER = models.CharField(max_length= 10)
    USER_EMAIL = models.EmailField()
    USER_DESCRIPTION = models.CharField(max_length = 1000)
    USER_MOTIVATION_LINE = models.CharField(max_length = 150)
    USER_PROFILE_IMAGE = models.ImageField(upload_to = 'USER_UPLOADS')
    USER = models.ForeignKey(User, on_delete=models.CASCADE)


class Breakfast(models.Model):
    IMAGE = models.ImageField(upload_to = 'Breakfast')
    FOOD = models.CharField(max_length = 20)
    DESCRIPTION = models.CharField(max_length = 100)
    PROTIEN = models.IntegerField()
    CARBOHYDRATE = models.IntegerField()
    FATS = models.IntegerField()
    ABOUT_USER = models.ForeignKey(About_User, on_delete = models.CASCADE)

class Lunch(models.Model):
    IMAGE = models.ImageField(upload_to = 'Lunch')
    FOOD = models.CharField(max_length = 20)
    DESCRIPTION = models.CharField(max_length = 100)
    PROTIEN = models.IntegerField()
    CARBOHYDRATE = models.IntegerField()
    FATS = models.IntegerField()
    ABOUT_USER = models.ForeignKey(About_User, on_delete = models.CASCADE)


class Dinner(models.Model):
    IMAGE = models.ImageField(upload_to = 'Dinner')
    FOOD = models.CharField(max_length = 20)
    DESCRIPTION = models.CharField(max_length = 100)
    PROTIEN = models.IntegerField()
    CARBOHYDRATE = models.IntegerField()
    FATS = models.IntegerField()
    ABOUT_USER = models.ForeignKey(About_User, on_delete = models.CASCADE)



class DIET_PLAN(models.Model):
    BREAKFAST = models.ForeignKey(Breakfast,on_delete = models.CASCADE)
    LUNCH = models.ForeignKey(Lunch,on_delete = models.CASCADE)
    DINNER = models.ForeignKey(Dinner,on_delete= models.CASCADE)
    ABOUT_USER = models.ForeignKey(About_User,on_delete = models.CASCADE)

class Exercises(models.Model):
    IMAGE = models.ImageField(upload_to = 'Exercise')
    EXERCISE_NAME = models.CharField(max_length = 20)
    DESCRIPTION = models.CharField(max_length = 50)
    ABOUT_USER = models.ForeignKey(About_User,on_delete = models.CASCADE)

class Event(models.Model):
    EVENT_NAME = models.CharField(max_length = 20)
    EVENT_DATE = models.DateField()
    EVENT_START_TIME = models.TimeField()
    EVENT_END_TIME = models.TimeField()
    EVENT_DESCRIPTION = models.CharField(max_length = 250)
    ABOUT_USER = models.ForeignKey(About_User,on_delete = models.CASCADE)


class User_Image(models.Model):
    IMAGE = models.ImageField(upload_to = 'USER_Images')
    CAPTION_IMAGE = models.CharField(max_length = 50, blank=True)
    ABOUT_USER = models.ForeignKey(About_User,on_delete = models.CASCADE)
    
