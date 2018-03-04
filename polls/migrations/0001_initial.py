# Generated by Django 2.0.1 on 2018-02-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=12)),
                ('total_votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(max_length=32)),
                ('voter_number', models.IntegerField()),
                ('address', models.CharField(max_length=120)),
                ('father_name', models.CharField(max_length=32)),
                ('sex', models.CharField(max_length=6)),
                ('date_of_birth', models.DateField()),
                ('vote_for', models.CharField(max_length=12)),
                ('vote_value', models.BooleanField()),
            ],
        ),
    ]
