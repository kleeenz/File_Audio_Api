# Generated by Django 3.1 on 2021-03-20 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioApi', '0002_auto_20210314_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songfile',
            old_name='sondID',
            new_name='songID',
        ),
        migrations.AlterField(
            model_name='audiobookfile',
            name='audioBookDuration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='podcastfile',
            name='podDuration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='songfile',
            name='songDuration',
            field=models.CharField(max_length=50),
        ),
    ]
