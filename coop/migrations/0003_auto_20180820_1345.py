# Generated by Django 2.0.5 on 2018-08-20 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0002_auto_20180819_0428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
