# Generated by Django 2.2 on 2019-04-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='deleted_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='prediction',
            field=models.ImageField(null=True, upload_to='predictions/'),
        ),
    ]
