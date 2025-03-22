from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    Username= models.CharField(max_length=16,unique=True)
    firstName= models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    email = models.EmailField(unique=True) 
    Password = models.CharField(max_length=16)
    profilePicture= models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
      return self.user.username
    


class Bookings(models.Model):
    bookingId= models.AutoField(primary_key=True)
    bookingDate= models.DateField()
    bookingTime= models.TimeField()
    partyMembers= models.IntegerField()
    surname= models.CharField(max_length=16)
    email = models.ForeignKey(UserProfile, to_field="email", on_delete=models.CASCADE, related_name="bookings_by_email")
    
    class Meta:
       verbose_name_plural = 'Bookings'
    
    def __str__(self):
      return f"{self.bookingDate} {self.bookingTime}"
  
class Reviews(models.Model):
    ReviewID= models.AutoField(primary_key=True)
    Title= models.CharField(max_length=30)
    RatingNum=models.IntegerField()
    ReviewText= models.CharField(max_length=1000)
    Username= models.ForeignKey(UserProfile, to_field="Username", on_delete=models.CASCADE, related_name="reviews_by_Username")
    
    class Meta:
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
      return f"{self.Title} - {self.Username}"

class Menu(models.Model):
    MenuID= models.AutoField(primary_key=True)
    MenuName= models.CharField(max_length=30)
    
    def __str__(self):
      return self.MenuName
    
class Item(models.Model):
    ItemID= models.AutoField(primary_key=True)
    ItemName= models.CharField(max_length=30)
    ItemPrice= models.DecimalField(max_digits=10, decimal_places=2)
    ItemDesc= models.CharField(max_length=100)
    SpiceLevel= models.IntegerField()
    MenuName= models.ForeignKey(Menu,on_delete=models.CASCADE)
    
    def __str__(self):
      return self.ItemName
    
    
    


