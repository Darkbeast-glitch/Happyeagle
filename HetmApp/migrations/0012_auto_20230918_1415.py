# Generated by Django 3.1.14 on 2023-09-18 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HetmApp', '0011_auto_20230918_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepackages',
            options={'ordering': ['date_added'], 'verbose_name': 'HomePackage', 'verbose_name_plural': 'HomePackages'},
        ),
        migrations.AlterModelOptions(
            name='mainpackageview',
            options={'ordering': ['date_added'], 'verbose_name': 'MainPackage', 'verbose_name_plural': 'MainPackages'},
        ),
    ]
