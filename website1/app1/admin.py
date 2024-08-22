from django.contrib import admin
from.models import Contact
from.models import Registration
from.models import Products
from.models import Cart
from.models import Category
from.models import Order
from.models import Wishlist
from.models import Notification
from.models import Adminregistration

# Register your models here.
admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Notification)
admin.site.register(Adminregistration)
