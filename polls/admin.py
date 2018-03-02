from django.contrib import admin

# Register your models here.
from .models import Voter, Party

admin.site.register(Voter)
admin.site.register(Party)