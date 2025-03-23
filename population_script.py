import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Book_A_Bite.settings')

import django
django.setup()
from BookaBite.models import UserProfile, Bookings, Reviews, Menu, Item
from django.contrib.auth.models import User
from datetime import date, time

def populate():
    main_items = [
        {'ItemName': 'Burger',
        'ItemPrice': 10.99,
        'ItemDesc': 'Beef Burger with lettuce, tomato, and a layer of mayonaise. Comes with fries',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Pizza',
        'ItemPrice': 12.99,
        'ItemDesc': 'Fresh baked tomato based pizza topped with cheese, basil, salami, and sweetcorn',
        'SpiceLevel': 2,
        },
        {'ItemName': 'Chicken Madras',
        'ItemPrice': 8.99,
        'ItemDesc': 'Spicy Indian curry that comes with rice.',
        'SpiceLevel': 5,
        },
        {'ItemName': 'Spicy Chicken Burger',
        'ItemPrice': 11.99,
        'ItemDesc': 'Chicken Burger with lettuce, tomato, and a layer of mayonaise. Comes with fries',
        'SpiceLevel': 4,
        },
        {'ItemName': 'Fish & Chips',
        'ItemPrice': 14.99,
        'ItemDesc': 'Large haddock fish and a porition of chips',
        'SpiceLevel': 1,
        }]
    
    kids_items = [
        {'ItemName': 'Kids Burger',
        'ItemPrice': 8.99,
        'ItemDesc': 'Beef Burger with ketchup. Comes with fries',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Pizza Rolls',
        'ItemPrice': 7.99,
        'ItemDesc': 'Fresh baked tomato based pizza rolls',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Child Curry',
        'ItemPrice': 8.99,
        'ItemDesc': 'Tame curry that comes with rice',
        'SpiceLevel': 2,
        },
        {'ItemName': 'Kids Chicken Burger',
        'ItemPrice': 8.99,
        'ItemDesc': 'Chicken Burger with ketchup. Comes with fries',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Small Fish & Chips',
        'ItemPrice': 10.99,
        'ItemDesc': 'Small haddock fish and a porition of chips',
        'SpiceLevel': 1,
        }]
    
    breakfast_items = [
        {'ItemName': 'Full Scottish Breakfast',
        'ItemPrice': 12.99,
        'ItemDesc': 'Breakfast with Lorne Sausage, Potato Scone, Haggis, Bacon, 2 Eggs, Beans and 2 slices of toast',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Full English Breakfast',
        'ItemPrice': 12.99,
        'ItemDesc': 'Breakfast with Sausages, Bacon, Mushrooms, Tomato, 2 Eggs, Beans and 2 slices of toast',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Eggs Benedict',
        'ItemPrice': 8.99,
        'ItemDesc': 'Two muffins topped with bacon and a poached egg',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Pancakes',
        'ItemPrice': 11.99,
        'ItemDesc': '3 fluffy pancakes that are topped with maple syrup and banana',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Breakfast Wrap',
        'ItemPrice': 9.99,
        'ItemDesc': 'Wrap that contains sausage, bacon, egg, hashbrowns, and ketchup',
        'SpiceLevel': 1,
        }]
    
    drink_items = [
        {'ItemName': 'Fresh Juice',
        'ItemPrice': 2.99,
        'ItemDesc': 'Apple Juice, Orange Juice, or Pineapple Juice',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Soft Drink',
        'ItemPrice': 3.99,
        'ItemDesc': 'Cola, Irn Bru, Lemonade, or Fanta',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Wine',
        'ItemPrice': 5.99,
        'ItemDesc': '250ml glass of either Red, White, or Rosey Wine',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Beer',
        'ItemPrice': 4.99,
        'ItemDesc': 'Choices of Corona, Guinness, Stella, or Heineken ',
        'SpiceLevel': 1,
        },
        {'ItemName': 'Cocktails',
        'ItemPrice': 7.99,
        'ItemDesc': 'Blue Lagoon, Purple Rain, Mojito, Martini, or Cosmopolitan',
        'SpiceLevel': 1,
        }]
    
    menus = {'Main': {'items': main_items},
             'Kids': {'items': kids_items},
             'Breakfast': {'items': breakfast_items},
             'Drinks': {'items': drink_items}}
    
    users = [
        {'username': 'Chef John',
        'firstName': 'John',
        'surname': 'Cheffy',
        'email': 'johncheffy@BookABite.com',
        'password': 'Password',
        },
        {'username': 'CoolGuy1',
        'firstName': 'Peter',
        'surname': 'Parker',
        'email': 'peterparker1@BookABite.com',
        'password': 'Password',
        }]
    
    resBookings = [
        {'bookingDate': date(2025, 3, 30),
        'bookingTime': time(18, 30),
        'partyMembers': 2,
        'surname': 'Cheffy',
        'email': 'johncheffy@BookABite.com',
        },
        {'bookingDate': date(2025, 4, 13),
        'bookingTime': time(15, 30),
        'partyMembers': 4,
        'surname': 'Parker',
        'email': 'peterparker1@BookABite.com',
        }]
    
    resReviews = [
        {'Title': 'Amazing Food!',
        'RatingNum': 5,
        'ReviewText': 'What a wonderful place to eat',
        'username': 'Chef John',
        },
        {'Title': 'Great Service',
        'RatingNum': 4,
        'ReviewText': 'Food slightly expensive but made up for by amazing service',
        'username': 'CoolGuy1',
        },
    ]
    
    for menu_name, menu_data in menus.items():
        menu_obj = add_menu(menu_name)
        for item in menu_data['items']:
            add_item(
                menu_obj,
                item['ItemName'],
                item['ItemPrice'],
                item['ItemDesc'],
                item['SpiceLevel']
            )

    for menu in Menu.objects.all():
        print(f"Menu: {menu}")
        for item in Item.objects.filter(MenuName=menu):
            print(f" - {item.ItemName}: £{item.ItemPrice}")
            
    for u in users:
        user_obj = User.objects.create_user(username=u['username'], password=u['password'])
        profile = UserProfile.objects.get_or_create(
            user=user_obj,
            Username=u['username'],
            firstName=u['firstName'],
            surname=u['surname'],
            email=u['email'],
            Password=u['password'], 
            profilePicture='' 
        )
    
    for b in resBookings:
        user_profile = UserProfile.objects.get(email=b['email'])
        Bookings.objects.create(
            bookingDate=b['bookingDate'],
            bookingTime=b['bookingTime'],
            partyMembers=b['partyMembers'],
            surname=b['surname'],
            email=user_profile
        )
    for r in resReviews:
        user_profile = UserProfile.objects.get(Username=r['username'])
        Reviews.objects.create(
            Title=r['Title'],
            RatingNum=r['RatingNum'],
            ReviewText=r['ReviewText'],
            Username=user_profile
        )

def add_item(menu_obj, ItemName, ItemPrice, ItemDesc, SpiceLevel):
    i, created = Item.objects.get_or_create(
        MenuName=menu_obj,
        ItemName=ItemName,
        defaults={
            'ItemPrice': ItemPrice,
            'ItemDesc': ItemDesc,
            'SpiceLevel': SpiceLevel
        }
    )
    if not created:
        i.ItemPrice = ItemPrice
        i.ItemDesc = ItemDesc
        i.SpiceLevel = SpiceLevel
        i.save()
    return i


def add_menu(MenuName):
    m = Menu.objects.get_or_create(MenuName=MenuName)[0]
    m.save()
    return m


if __name__ == '__main__':
    print('Starting BookABite population script...')
    populate()
    