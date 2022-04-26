from django.contrib import admin

# Register your models here.
from django.contrib import admin

from User.models import Bider, Customer, User

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Bider)

