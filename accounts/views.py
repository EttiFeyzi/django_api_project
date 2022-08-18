from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth import login
from accounts.models import MyUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.forms import RegisterForm
from accounts import helper
from rest_framework.decorators import api_view
from rest_framework.response import Response

    

def register_view(request):
    form = RegisterForm
    if request.method == "POST":
        try:
            if 'mobile' in request.POST:
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                #send otp
                otp = helper.get_random_otp()
                helper.send_otp(mobile, otp)
                user.otp = otp
                user.save()
                print(otp)
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify'))
                

        except MyUser.DoesNotExist:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                #send otp
                otp = helper.get_random_otp()
                helper.send_otp(mobile, otp)
                user.otp = otp
                user.is_active = False
                user.save()
                print(otp)
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify'))

    return render(request, 'register.html', {'form':form})




def verify(request):
    try:

        mobile = request.session.get('user_mobile')
        user = MyUser.objects.get(mobile = mobile)

        if request.method == "POST":

            # chec 0tp expiration
            if not helper.chek_otp_expiration(user.mobile):
                return HttpResponseRedirect(reverse('register_view'))


            if user.otp != int(request.POST.get('otp')):
                return HttpResponseRedirect(reverse('register_view'))
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        return render(request, 'verify.html', {'mobile':mobile})

    except MyUser.DoesNotExist:
        return HttpResponseRedirect(reverse('register_view'))
    




#  your views here.

# def mobile_login(request):
    # if request.method == "POST":
        # if 'mobile' in  request.POST:
            # mobile = request.POST.get('mobile')
            # user = MyUser.objects.get(mobile=mobile)
            # login(request, user)
            # return HttpResponseRedirect(reverse('dashboard'))

    # return render(request, 'mobile_login.html')

def dashboard(request):
    return render(request, 'dashboard.html')


