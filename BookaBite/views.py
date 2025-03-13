from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'BookaBite/home.html')

def about(request):
    return render(request, 'BookaBite/about.html')

def login(request):
    return render(request, 'BookaBite/login.html')

def signup(request):
    return render(request, 'BookaBite/signup.html')

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
