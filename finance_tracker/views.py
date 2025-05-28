from django.shortcuts import redirect, render
from django.views import View
from finance_tracker.forms import RegisterForm
from django.contrib.auth import login


class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form = RegisterForm()
        return render (request,'register.html',
        {"form":form},)
    
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            login(request,user)
            redirect("")