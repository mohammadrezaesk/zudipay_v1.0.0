from django.conf.urls import url,include
from django.urls import path

from . import views
urlpatterns=[
    url(r'^$', views.havaleform,name = 'havale_form'),
    path('<company>/<az>/<be>/<int:count>/<int:day>/<int:month>/',views.payform),
]
