from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from BookaBite.forms import UserForm,UserProfileForm,ReviewsForm,BookingsForm,MenuForm,ItemForm
from django.urls import reverse
from django.shortcuts import redirect
from BookaBite.models import Reviews, Bookings, UserProfile, Menu, Item
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from datetime import date

# Create your views here.
def home(request):
    return render(request, 'BookaBite/home.html')

def about(request):
    return render(request, 'BookaBite/about.html')

@login_required
def user_logout(request):
    
    logout(request)
    #request.session.flush()
    return redirect(reverse('BookABite:home'))
    

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
            profile = profile_form.save(commit=False)
            profile.user = user
            
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
@login_required
def bookings(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'Username': user.username, 
                'firstName': user.first_name, 
                'surname': user.last_name, 
                'email': user.email
                }
            )
        
    user_bookings = Bookings.objects.filter(
        email=user_profile,  
        bookingDate__gte=now().date()
    ).order_by('bookingDate', 'bookingTime')  
    
    return render(request, 'BookaBite/bookings.html',{'user_Bookings': user_bookings})

@login_required
def manageBooking(request):
    user = request.user
    
    user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'Username': user.username, 
                'firstName': user.first_name, 
                'surname': user.last_name, 
                'email': user.email
                }
            )
    user_bookings = Bookings.objects.filter(email=user_profile)
    user_bookings = user_bookings.filter(bookingDate__gte=date.today())
    
    
    return render(request, 'BookaBite/manageBookings.html',{'user_bookings': user_bookings})

@login_required
def addBooking(request):
    user = request.user
    
    form = BookingsForm(request.POST)
    user_profile, created = UserProfile.objects.get_or_create(
        user=user,
        defaults={
            'Username': user.username,
            'firstName': user.first_name,
            'surname': user.last_name,
            'email': user.email
        }
    )
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.email = user_profile  
            booking.save()
            return redirect('BookABite:bookings')  
    else:
        form = BookingsForm()
        
    
    return render(request, 'BookaBite/addBookings.html',{'form': form})

@login_required
def editBooking(request, booking_id):
    booking = get_object_or_404(Bookings, bookingId=booking_id)
    
    if request.user.userprofile.email != booking.email.email:
        return redirect('BookABite:bookings')
    
    
    if request.method == "POST":
        form = BookingsForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('BookABite:bookings')  
    else:
        form = BookingsForm(instance=booking)
    return render(request, 'BookaBite/editBooking.html', {'form': form, 'booking': booking})


@login_required
def deleteBooking(request, booking_id):
    
    booking = get_object_or_404(Bookings, bookingId=booking_id)
    
    if booking.email.user != request.user:
        return redirect('BookABite:manageBooking')
    
    if request.method == "POST":
        booking.delete()  
        return redirect('BookABite:manageBooking')
    
    return render(request, 'BookaBite/deleteBooking.html', {'booking': booking})
    
    
        
    
    

def menu(request):
    return render(request, 'BookaBite/menu.html')

def chooseMenu(request):
    menus = Menu.objects.all()
    return render(request, 'BookaBite/chooseMenu.html', {'menus': menus})

def showMenu(request, menu):
    
    context_dict = {}
    
    try:
        menu_obj = Menu.objects.get(MenuName = menu)
        
        items = Item.objects.filter(MenuName = menu_obj)
        
        context_dict['items'] = items
        
        context_dict['menu'] = menu_obj
    except Menu.DoesNotExist:
        
        context_dict['items'] = None
        context_dict['menu'] = None
        
    return render(request, 'BookaBite/showMenu.html', context=context_dict)

def addMenu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookABite:chooseMenu')
    else:
        form = MenuForm()

    return render(request, 'BookaBite/addMenu.html', {'form': form})


def addItem(request):
    print("🚀 addItem view was called!")

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('BookABite:showMenu', item.MenuName.MenuName)
    else:
        form = ItemForm()

    return render(request, 'BookaBite/addItem.html', {'form': form})


def review(request):
    
    Review_list= Reviews.objects.order_by('RatingNum')
    context_dict = {}
    context_dict['review_list']= Review_list
    
    return render(request, 'BookaBite/review.html',context_dict)

@login_required
def addReview(request):
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            user= request.user
            user_profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'Username': user.username, 
                    'firstName': user.first_name, 
                    'surname': user.last_name, 
                    'email': user.email
                }
            )

            review.Username = user_profile
            review.save()  
            return redirect('BookABite:review')
    else:
        form = ReviewsForm()
    return render(request, 'BookaBite/addReview.html', {'form': form})

@login_required
def manageReview(request):
    user = request.user
    
    user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'Username': user.username, 
                'firstName': user.first_name, 
                'surname': user.last_name, 
                'email': user.email
                }
            )
    user_reviews = Reviews.objects.filter(Username=user_profile)
    
    
    return render(request, 'BookaBite/manageReview.html',{'user_reviews': user_reviews})

@login_required
def deleteReview(request,review_id):
    review = get_object_or_404(Reviews, ReviewID=review_id, Username=request.user.userprofile)
    if request.method == "POST":
        review.delete()
        return redirect('BookABite:manageReview')
    return render(request, 'BookaBite/deleteReview.html', {'review': review})

@login_required
def editReview(request, review_id):
    review = get_object_or_404(Reviews, ReviewID=review_id, Username=request.user.userprofile)
    if request.method == "POST":
        form = ReviewsForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('BookABite:manageReview')
    else:
        form = ReviewsForm(instance=review) 
    return render(request, 'BookaBite/editReview.html', {'form': form, 'review': review})