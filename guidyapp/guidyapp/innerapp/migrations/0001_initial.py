# Generated by Django 2.0.2 on 2018-02-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('info', models.TextField(blank=True, null=True)),
                ('login', models.TextField(blank=True, null=True, unique=True)),
                ('language', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'guide',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('guide_id', models.IntegerField(blank=True, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('date_start', models.TextField(blank=True, null=True)),
                ('date_finish', models.TextField(blank=True, null=True)),
                ('spots', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(unique=True)),
                ('location', models.TextField()),
                ('time', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tour',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('login', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'tourist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TouristTour',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('tourist_id', models.IntegerField(blank=True, null=True)),
                ('tour_id', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tourist_tour',
                'managed': False,
            },
        ),
    ]