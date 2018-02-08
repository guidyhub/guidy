# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_avatar(sender, instance, created, **kwargs):
    if created:
        Avatar.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_avatar(sender, instance, **kwargs):
    instance.avatar.save()

class Guide(models.Model):
    # id = models.IntegerField(blank=True, primary_key=True)
    info = models.TextField(blank=True, null=True)
    login = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    language = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    photo = models.FilePathField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'guide'

def get_image_path(instance, filename):
    return os.path.join('imgs', str(instance.id), filename)

class Tour(models.Model):
    # id = models.IntegerField(blank=True, primary_key=True)
    # guide_id = models.IntegerField(blank=True, null=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    info = models.TextField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)  # This field type is a guess.
    date_finish = models.DateField(blank=True, null=True)  # This field type is a guess.
    spots = models.IntegerField(blank=True, null=True)
    name = models.TextField(unique=True)  # This field type is a guess.
    location = models.TextField()  # This field type is a guess.
    time = models.TimeField(blank=True, null=True)  # This field type is a guess.
    price = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    # Tour members
    members = models.ManyToManyField(User, through='TouristTour')

    class Meta:
        # managed = False
        db_table = 'tour'



# class Tourist(models.Model):
#     # id = models.IntegerField(blank=True, primary_key=True)
#     login = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'tourist'


class TouristTour(models.Model):
    # id = models.IntegerField(blank=True, primary_key=True)
    # tourist_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # tour_id = models.IntegerField(blank=True, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'tourist_tour'
