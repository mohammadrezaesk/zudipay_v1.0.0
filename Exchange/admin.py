from django.contrib import admin
from .models import pricecard
# Register your models here.
class pricecardclass(admin.ModelAdmin):
    list_display = ('country','city','type','price','ishow')
admin.site.register(pricecard,pricecardclass)
