from django.urls import path
from BookaBite import views

app_name = 'BookABite'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name="signup"),
    path('bookings/', views.bookings, name="bookings"),
    path('bookings/ManageBookings/', views.manageBooking, name='manageBooking'),
    path('bookings/AddBookings/', views.addBooking, name='addBooking'),
    path('menu/', views.menu, name='menu'),
    path('menu/chooseMenu', views.chooseMenu, name="chooseMenu"),
    path('menu/chooseMenu/showMenu', views.showMenu, name="showMenu"),
    path('menu/chooseMenu/addMenu', views.addMenu, name="addMenu"),
    path('menu/chooseMenu/showMenu/addItem', views.addItem, name="addItem"),
    path('review/', views.review, name="review"),
    path('review/addReview', views.addReview, name="addReview"),
    path('review/manageReview', views.manageReview, name="manageReview"),
    path('logout/', views.user_logout, name='logout'),
]
