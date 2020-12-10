from django.db import models
from django.contrib.auth.models import User


#Here in django, tables are called as models
#No need of seperate SQL Developer to design DB schema


#This is the table for customer details
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



#Location restaurant model is for to query restaurants based on searched location, and if no location matched , no object will be returned
class Location_Restaurant(models.Model):
  Location = models.CharField(max_length=50)
  Restaurant_Name = models.CharField(max_length=50)
  Manager_Name = models.CharField(max_length=50)
  Restaurant_Id = models.CharField(max_length=20)

  def __str__(self):
    return self.Location + self.Restaurant_Name

 

#Restaurant Food model is for showing food of particular restaurant after querying up through location using forms
class Restaurant_Food_New(models.Model):
  Restaurant_Id = models.ForeignKey(Location_Restaurant, on_delete=models.CASCADE)
  Food_Name = models.CharField(max_length=50)
  Category = models.CharField(max_length=30)
  Price = models.IntegerField()
  
  def __str__(self):
    return self.Food_Name + str(self.Price)

