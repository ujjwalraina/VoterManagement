from django.shortcuts import render
from rest_framework.decorators import api_view

from .serializers import VoterSerializer
# Create your views here.
from django.http import HttpResponse
from .models import Voter,Party
from rest_framework.response import Response

def index(request):
    return render(request,'index.html')

def details(request):
    return render(request,'details.html')

def result(request):
    number = request.POST.get("voter_number")
    V = Voter.objects.filter(voter_number=number)
    if V.count() == 1:
        a = []
        a = V.values_list()
        name = a[0][1]
        address = a[0][3]
        father_name = a[0][4]
        sex = a[0][5]
        date_of_birth = a[0][6]
        str1 = "<h1>Details of voter-number: " + number + "\n</h1>"
        str2 = "<p>Voter-name: " + name + "\n</p>"
        str3 = "<p>Address: " + address + "\n</p>"
        str4 = "<p>Father-name: " + father_name + "\n</p>"
        str5 = "<p>Sex: " + sex + "\n</p>"
        str6 = "<p>Date of birth: " + str(date_of_birth) + "\n</p>"
        detail = str1 + str2 + str3 + str4 + str5 + str6
        return HttpResponse(detail)
    else:
        return HttpResponse("The voter number you have entered is incorrect")


def sign(request):
    return render(request,'signup.html')

def vote(request):
    number = request.POST.get('voterid')
    v = Voter.objects.filter(voter_number=number)
    v.vote_value = True
    party = request.POST.get("party")
    v.vote_for = party
    v.update(vote_value=True,vote_for=party)
    return HttpResponse("Thank you for casting your vote")

def signup(request):
    if request.method == "POST":
        V = Voter()
        name = request.POST.get("voter_name")
        number = request.POST.get("voter_number")
        address = request.POST.get("address")
        fname = request.POST.get("father_name")
        sex = request.POST.get("sex")
        dob = request.POST.get("date_of_birth")
        V.voter_name = name
        V.voter_number = number
        V.address = address
        V.father_name = fname
        V.sex = sex
        V.date_of_birth = dob
        V.vote_value = False
        V.vote_for = "None"
        V.save()
        return render(request, 'index.html')
    else:
        return HttpResponse('You have clicked on button through get method')

def login(request):
    if request.method == 'POST':
        name = request.POST.get("voter_name")
        number = request.POST.get("voter_number")
        sc = Voter.objects.filter(voter_number=number,voter_name=name)
        if sc.count()== 1:
            return render(request, 'vote.html', {'number': str(number)},print({number}))
        else:
            return HttpResponse('Username or password is wrong')
    else:
        return HttpResponse('You have clicked on button through get method')