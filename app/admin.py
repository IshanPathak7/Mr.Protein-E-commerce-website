from django.contrib import admin
from django.contrib.auth.models import User
from .models import *




admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderPlaced)
admin.site.register(Category)
admin.site.register(Tutorial)
admin.site.register(Exercise)
