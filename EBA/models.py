from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
  GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  confirm_password = models.CharField(max_length=30)
  

  def __str__(self):
    return self.user.username


class Location_Restaurant(models.Model):
  Location = models.CharField(max_length=50)
  Restaurant_Name = models.CharField(max_length=50)
  Manager_Name = models.CharField(max_length=50)
  Restaurant_Id = models.CharField(max_length=20)

  def __str__(self):
    return self.Location + self.Restaurant_Name

class Restaurant_Food_New(models.Model):
  Restaurant_Id = models.ForeignKey(Location_Restaurant, on_delete=models.CASCADE)
  Food_Name = models.CharField(max_length=50)
  Category = models.CharField(max_length=30)
  Price = models.IntegerField()
  
  def __str__(self):
    return self.Food_Name + str(self.Price)

