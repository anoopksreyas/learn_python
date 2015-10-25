from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    COUNTRIES = (('IN', 'India'), ('USA', 'America'))
    
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length = 50, verbose_name='First name')
    last_name = models.CharField(max_length = 50, verbose_name='Last name')
    occupation = models.CharField(max_length = 50)
    hobbies = models.CharField(max_length = 50)
    husband_name = models.CharField(max_length = 50)
    country = models.CharField(max_length=10, choices= COUNTRIES, default = 'India')
    state = models.CharField(max_length=10)
    city = models.CharField(max_length = 10)
    number_of_kids = models.IntegerField()