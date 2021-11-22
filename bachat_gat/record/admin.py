from django.contrib import admin
from .models import UserDetails,UserName,MonthName,Calculation

# Register your models here.
class UserDeatailsAdmin(admin.ModelAdmin):
    list_display = ['month','username','saving','intrest','paidLoan','borrowLoan','fine']

class UserNameAdmin(admin.ModelAdmin):
    list_display = ['name','mobile']

class MonthNameAdmin(admin.ModelAdmin):
    list_display = ['month']

class CalculationAdmin(admin.ModelAdmin):
    list_display = ['totalAmount','availableAmount']
admin.site.register(UserDetails,UserDeatailsAdmin)
admin.site.register(UserName,UserNameAdmin)
admin.site.register(MonthName,MonthNameAdmin)
admin.site.register(Calculation,CalculationAdmin)



