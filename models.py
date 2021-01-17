# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

class Clubs(models.Model):
    clubs_id = models.AutoField(db_column='Id', primary_key=True)
    firstname = models.CharField(db_column='Firstname', unique=True, max_length=50)  # Field name made lowercase.
    clubtype = models.IntegerField(db_column='ClubType')  # Field name made lowercase.
    tagline = models.CharField(db_column='Tagline', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    links = models.TextField(db_column='Links')  # Field name made lowercase.
    leader_id = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    adress = models.TextField(db_column='Adress')  # Field name made lowercase.
    meeting = models.DateField(db_column='Meeting', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')
