from django.conf.urls import url,include
from . import views
urlpatterns=[
    url(r'^change/$', views.changecard,name = 'changecard'),
    url(r'^login/$', views.login,name = 'login')
]
