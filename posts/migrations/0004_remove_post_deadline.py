# Generated by Django 2.0 on 2017-12-29 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20171229_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='deadline',
        ),
    ]