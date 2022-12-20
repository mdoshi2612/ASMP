# Generated by Django 3.2.6 on 2021-08-20 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=20)),
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('rollno', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('contactno', models.CharField(blank=True, max_length=100)),
                ('personalEmail', models.CharField(blank=True, default='', max_length=100)),
                ('sop', models.CharField(blank=True, max_length=500)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('experience', models.CharField(blank=True, max_length=500)),
                ('goal', models.CharField(blank=True, max_length=500)),
                ('obstacle', models.CharField(blank=True, max_length=500)),
                ('pref_1', models.IntegerField(blank=True, null=True)),
                ('pref_2', models.IntegerField(blank=True, null=True)),
                ('pref_3', models.IntegerField(blank=True, null=True)),
                ('pref_4', models.IntegerField(blank=True, null=True)),
                ('pref_5', models.IntegerField(blank=True, null=True)),
                ('submitted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_id', models.CharField(max_length=10)),
                ('gender', models.CharField(default='Male', max_length=10)),
                ('year', models.CharField(default='2018', max_length=20)),
                ('department', models.CharField(default='Civil', max_length=100)),
                ('degree', models.CharField(default='BTech', max_length=100)),
                ('city', models.CharField(default='Mumbai', max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('discp', models.TextField(blank=True)),
                ('interest', models.CharField(max_length=200, null=True)),
                ('maxmentees', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0.0)),
                ('available', models.BooleanField(default=True)),
                ('maxscore', models.FloatField(default=0.0)),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]