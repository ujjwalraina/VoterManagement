# Generated by Django 2.0.1 on 2018-02-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180227_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='vote_for',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='voter',
            name='vote_value',
            field=models.BooleanField(),
        ),
    ]
