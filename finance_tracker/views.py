from django.shortcuts import render
from django.views import View
from finance_tracker.forms import RegisterForm

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form = RegisterForm()
        return render (request,'register.html',
        {"form":form},)
