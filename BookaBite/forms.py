from django.contrib.auth.models import User
from BookaBite.models import UserProfile, Reviews, Bookings
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields= ('username', 'email' ,'password',)
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'surname','profilePicture',)
        
class ReviewsForm(forms.ModelForm):
    Title= forms.CharField(max_length=30,help_text="Enter a title for your review")
    RatingNum =  forms.IntegerField(
        min_value=1, 
        max_value=5,
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 6)])
    )
    
    ReviewText= forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),help_text="Enter review here")
    
    class Meta:
        model = Reviews  
        fields = ['Title', 'RatingNum', 'ReviewText'] 

class BookingsForm(forms.ModelForm):
    bookingDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    bookingTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = Bookings
        fields = ['bookingDate', 'bookingTime', 'partyMembers', 'surname']
