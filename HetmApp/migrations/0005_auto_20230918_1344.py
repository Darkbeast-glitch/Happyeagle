# Generated by Django 3.1.14 on 2023-09-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HetmApp', '0004_homepackages_home'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepackages',
            name='date',
        ),
        migrations.RemoveField(
            model_name='homepackages',
            name='home',
        ),
        migrations.AddField(
            model_name='homepackages',
            name='packages_include_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepackages',
            name='packages_include_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepackages',
            name='packages_include_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepackages',
            name='packages_include_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepackages',
            name='packages_include_5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mainpackageview',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
