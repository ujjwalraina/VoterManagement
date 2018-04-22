from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Voter, Party
import datetime
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def details(request):
    return render(request,'details.html')

def result(request):
    count,count1, count2, count3 = 0,0,0,0
    party1, party2, party3 = "BJP", "CONGRESS", "AAP"
    V1 = Voter.objects.filter(vote_for=party1)
    count1 = V1.count()
    V2 = Voter.objects.filter(vote_for=party2)
    count2 = V2.count()
    V3 = Voter.objects.filter(vote_for=party3)
    count3 = V3.count()
    count = max(count1,count2,count3)
    if count == count1:
        statement0 = "<h1>RESULTS: "+str(party1)+" won the election.</h1>"
    elif count == count2:
        statement0 = "<h1>RESULTS: " + str(party2) + " won the election.</h1>"
    elif count == count3:
        statement0 = "<h1>RESULTS: " + str(party3) + " won the election.</h1>"
    else:
        statement0 = "No single party got the majority."
    statement1 = "<p>"+str(party1)+" got "+str(count1)+ " votes.\n</p>"
    statement2 = "<p>"+str(party2) + " got " + str(count2) + " votes.\n</p>"
    statement3 = "<p>"+str(party3) + " got " + str(count3) + " votes.\n</p>"
    statement = statement0+statement1+statement2+statement3
    return HttpResponse(statement)

def voterinfo(request):
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
    party = request.POST.get("party")
    v.update(vote_value=True,vote_for=party)
    data1 = request.COOKIES['uid']
    data2 = request.COOKIES['name']
    logintime=request.COOKIES['logintime']

    #email
    subject = "Election log"
    message = "The following user has casted his vote: "+str(data1)+" "+str(data2)
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_TO_LIST,settings.EMAIL_HOST_USER]
    send_mail(subject,message,from_email,to_list,fail_silently=True)
    return HttpResponse("Thank you for casting your vote: "+str(data2)+" | login time "+str(logintime) +" "+message)


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
        return HttpResponse('Sigmup Completed')
    else:
        return HttpResponse('You have clicked on button through get method')

def login(request):
    if request.method == 'POST':
        name = request.POST.get("voter_name")
        number = request.POST.get("voter_number")
        sc = Voter.objects.filter(voter_number=number,voter_name=name,vote_value=False)
        if sc.count()== 1:
            reponse = render(request, 'vote.html', {'number': str(number)}) #response is a variable which stores an object
            reponse.set_cookie('uid',str(number),6000) #uid is key which works like global variable , and name is data
            reponse.set_cookie('name',name, 6000)
            reponse.set_cookie('logintime', datetime.datetime.now())
            return reponse
        else:
            return HttpResponse('Username-password combination entered wrong OR Voter has already casted his vote')
    else:
        return HttpResponse('You have clicked on button through get method')