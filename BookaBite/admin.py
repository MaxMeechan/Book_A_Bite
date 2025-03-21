from django.contrib import admin
from BookaBite.models import Reviews, Bookings, UserProfile, Menu, Item

# Register your models here.
admin.site.register(Reviews)
admin.site.register(Bookings)
admin.site.register(UserProfile)
admin.site.register(Menu)
admin.site.register(Item)