from django.db import models

# Create your models here.
class Party(models.Model):
    party_name = models.CharField(max_length=12)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return  self.party_name


class Voter(models.Model):
    voter_name = models.CharField(max_length=32)
    voter_number = models.IntegerField()
    address = models.CharField(max_length=120)
    father_name = models.CharField(max_length=32)
    sex = models.CharField(max_length=6)
    date_of_birth = models.DateField()
    vote_for = models.CharField(max_length=20)
    vote_value = models.BooleanField(default=False)

    def __str__(self):
        return  self.voter_name