# Generated by Django 3.2.5 on 2021-07-25 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2021, 7, 25, 13, 43, 25, 56667, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, '남성'), (1, '여성')], default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.IntegerField(choices=[(0, '초등학생'), (1, '중학생'), (2, '고등학생'), (3, '대학생'), (4, '직장인'), (5, '무직')], default=5),
        ),
    ]