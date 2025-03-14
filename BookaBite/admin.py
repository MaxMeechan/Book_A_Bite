from django.contrib import admin
from BookaBite.models import Reviews, Bookings, User, Menu, Item

# Register your models here.
admin.site.register(Reviews)
admin.site.register(Bookings)
admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Item)