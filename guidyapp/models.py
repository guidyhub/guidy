# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Guide(models.Model):
    id = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    login = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    language = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    photo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'guide'


class Tour(models.Model):
    id = models.IntegerField(blank=True, null=True)
    guide_id = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    date_start = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_finish = models.TextField(blank=True, null=True)  # This field type is a guess.
    spots = models.IntegerField(blank=True, null=True)
    name = models.TextField(unique=True)  # This field type is a guess.
    location = models.TextField()  # This field type is a guess.
    time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tour'


class Tourist(models.Model):
    id = models.IntegerField(blank=True, null=True)
    login = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tourist'


class TouristTour(models.Model):
    id = models.IntegerField(blank=True, null=True)
    tourist_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tourist_tour'
