from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import date, datetime
from time import strptime

# Create your models here.
class FormManager(models.Manager):
    def registration_validator(self, postData):
        errors={}
        if len(postData["name"]) < 3:
            errors["name"] = "First Name should be at least 3 characters"
        if len(postData["username"]) < 3:
            errors["username"] = "Last Name should be at least 3 characters"
        else: 
            username_taken = User.objects.filter(username = postData['username'])
            if len(username_taken) > 0:
                errors['username_taken'] = "This username is alredy taken! Try another one"
        if len(postData["password"]) < 8:
            errors["password"] = "Too short! Password should be at least 8 characters"
        if postData["password"] != postData["password_repeat"]:
            errors["password_repeat"] = "Ooops! Password doesn't match! Try one more time!"
        return errors

    def login_validator(self, postData):
        errors={}
        userinDB = User.objects.filter(username = postData['username'])
        if len(userinDB) == 0:
            print("USERNAME IS NOT REGISTERED")
            errors["username_exist"] = "Wrong username"
        else:
            user = userinDB[0]
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                print("password match")
            else:
                errors["incorect_password"] = "Wrong password"
                print("failed password")
        print (userinDB)
        return errors

class TripManager(models.Manager):
    def tripValidator(self, postData):
        errors={}
        if len(postData['destination']) < 1:
            errors['destination'] = "Enter your destination"
        if len(postData['plan']) < 1:
            errors['plan'] = "Description must be provided"
        if len(postData['startDate']) < 3:
            errors['desc_len'] = "Description must be at least 3 characters"
        if str(date.today()) > str(postData['startDate']):
            errors["invalid_date"] = "Please input a valid Date. Note: Start time can not be in the past."
        if str(date.today()) > postData['endDate']:
            errors["invalid_date_future"] = "Please input a valid Date. Note: End date must be in the future"
        if postData['startDate'] > postData['endDate']:
            errors["invalid_date_future_and_end"] = "Travel Date From can not be in the future of Travel Date To"
        
        # newtrip = Trip.objects.create (destination = postData['destination'], startDate = postData['startDate'],endDate= postData['endDate'], plan = postData['plan'], creator = User.objects.get(id = postData['userid']))
        # newtrip.joiner.add(User.objects.get(id = postData['user_id']))
        # newtrip.save()
        
        return errors



class User (models.Model):
    name = models.CharField(max_length=225)
    username = models.CharField(max_length=225)
    password =  models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager()

class Trip (models.Model):
    destination = models.CharField(max_length=225)
    startDate = models.DateField()
    endDate = models.DateField()
    plan =  models.TextField()
    creator = models.ForeignKey(User, related_name="travel", on_delete = models.CASCADE)
    join = models.ManyToManyField(User, related_name="joiner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
