# Generated by Django 3.1.14 on 2023-09-18 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HetmApp', '0010_auto_20230918_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepackages',
            options={'ordering': ['theDate'], 'verbose_name': 'HomePackage', 'verbose_name_plural': 'HomePackages'},
        ),
        migrations.AlterModelOptions(
            name='mainpackageview',
            options={'ordering': ['theDate'], 'verbose_name': 'MainPackage', 'verbose_name_plural': 'MainPackages'},
        ),
        migrations.RemoveField(
            model_name='tourpackages',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='tourpackages',
            name='theDate',
        ),
    ]
