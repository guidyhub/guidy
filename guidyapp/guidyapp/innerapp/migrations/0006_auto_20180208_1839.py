# Generated by Django 2.0.2 on 2018-02-08 16:39

from django.db import migrations, models
import guidyapp.innerapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('innerapp', '0005_auto_20180208_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=guidyapp.innerapp.models.get_image_path),
        ),
    ]
