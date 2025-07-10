from django.shortcuts import render
from django_otp.decorators import otp_required

@otp_required
def index(request):
    return render(request, "mainapp/index.html")