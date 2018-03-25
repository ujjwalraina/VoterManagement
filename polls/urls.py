from django.conf.urls import url
from . import views

urlpatterns = [
    # /polls/
    url(r'^$', views.index, name = 'index'),
    url(r'signup/', views.signup, name='signup'),
    url(r'login/', views.login, name='login'),
    url(r'vote/', views.vote, name='vote'),
    url(r'signup.html/', views.sign, name='sign'),
    url(r'details.html/', views.details, name ='details'),
    url(r'voterinfo/', views.voterinfo, name ='voterinfo'),
    url(r'result/', views.result, name ='result'),
]
