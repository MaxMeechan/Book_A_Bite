from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from BookaBite.forms import UserForm,UserProfileForm
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'BookaBite/home.html')

def about(request):
    return render(request, 'BookaBite/about.html')

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect('BookABite:home')
            else:
                return HttpResponse("Your FusionFeast: BookaBite account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'BookaBite/login.html')
        

def signup(request):
    registered=False
    if request.method == 'POST':
        user_form =UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user =user_form.save()
            user.set_password(user.password)
            user.save()
            profile =profile_form.save(commit=False)
            profile.user =user
            
            if 'picture' in request.FILES:
                profile.picture =request.FILES['picture']
            
            profile.save()
            registered= True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form =UserForm()
        profile_form=UserProfileForm()
                
    
    
    return render(request, 'BookaBite/signup.html',context={'user_form': user_form, 'profile_form': profile_form, 'registered' :registered})

def bookings(request):
    return render(request, 'BookaBite/bookings.html')

def manageBooking(request):
    return render(request, 'BookaBite/manageBookings.html')

def addBooking(request):
    return render(request, 'BookaBite/addBookings.html')

def menu(request):
    return render(request, 'BookaBite/menu.html')

def chooseMenu(request):
    return render(request, 'BookaBite/chooseMenu.html')

def showMenu(request):
    return render(request, 'BookaBite/showMenu.html')

def addMenu(request):
    return render(request, 'BookaBite/addMenu.html')

def addItem(request):
    return render(request, 'BookaBite/addItem.html')

def review(request):
    return render(request, 'BookaBite/review.html')

def addReview(request):
    return render(request, 'BookaBite/addReview.html')

def manageReview(request):
    return render(request, 'BookaBite/manageReview.html')
