from django.contrib import admin
from .models import User,Category,Listing,Logs,Rentlist
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Logs)
admin.site.register(Rentlist)
