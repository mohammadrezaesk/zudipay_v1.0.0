from django.contrib import admin

from .models import tour,traveler
# Register your models here.
class tourclass(admin.ModelAdmin):
    list_display = ('tourleader','phone','origin','destination','day','month','company')
class travelerclass(admin.ModelAdmin):
    list_display = ('touri','firstname','lastname','birthday','birthmonth','birthyear','passport','gender','ischild')
admin.site.register(tour,tourclass)
admin.site.register(traveler,travelerclass)
