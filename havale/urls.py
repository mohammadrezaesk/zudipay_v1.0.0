from django.conf.urls import url,include
from . import views
urlpatterns=[
    url(r'^$', views.havaleform,name = 'havale_form')
]
