# Generated by Django 2.0.5 on 2018-09-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0010_remove_userinfo_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='home_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='office_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='town',
            field=models.CharField(max_length=20),
        ),
    ]