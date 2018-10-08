from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Image,User,Profile
from .forms import NewImageForm,NewProfileForm

@login_required(login_url='/accounts/login/')
def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{'images':images,})
@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('Home')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})
@login_required(login_url="/accounts/login/")
def like(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)

    if operation == 'like':

        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('Home')
@login_required(login_url="/accounts/login/")
def profile(request):
    profile=Profile.objects.filter(user=request.user.id)
    images=Image.objects.filter(user=request.user.id)
    return render (request,'profile.html',{'images':images,'profile':profile})
@login_required(login_url="/accounts/login/")
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})
