from rest_framework import serializers
from .models import Voter,Party

class VoterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voter
        #fields = ('voter_name','voter_number','address','father_name','sex','date_of_birth','vote_for','vote_value')
        fields = '__all__'