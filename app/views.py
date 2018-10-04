from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image

@login_required(login_url='/accounts/login/')
def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{'images':images,})
