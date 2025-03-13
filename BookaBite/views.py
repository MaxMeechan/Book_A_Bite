from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Book a Bite Home Page")

def about(request):
    return HttpResponse("This is the About Page")

def login(request):
    return HttpResponse("Login Page")

def signup(request):
    return HttpResponse("Sign Up Page")

def bookings(request):
    return HttpResponse("Booking Page")

def manageBooking(request):
    return HttpResponse("Manage Booking Page")

def addBooking(request):
    return HttpResponse("Add Booking Page")

def menu(request):
    return HttpResponse("Menu Page")

def chooseMenu(request):
    return HttpResponse("Choose Menu Page")

def showMenu(request):
    return HttpResponse("Show Menus Page")

def addMenu(request):
    return HttpResponse("Add Menu Page")

def addItem(request):
    return HttpResponse("Add Item Page")

def review(request):
    return HttpResponse("Review Page")

def addReview(request):
    return HttpResponse("Add Review Page")

def manageReview(request):
    return HttpResponse("Manage Review Page")
