# Generated by Django 2.0 on 2017-12-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='days_taken',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
