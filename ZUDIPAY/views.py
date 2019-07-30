from django.shortcuts import render
from havale.models import tour , traveler

def home(request):
    args={}
    return render(request,'zudipay/home.html',args)
def about(request):
    args={}
    return render(request,'zudipay/about.html',args)
def fadakpage(request):
    tours = tour.objects.order_by('tourleader')
    travelers = traveler.objects.order_by('touri')
    j=0
    for i in tours:
        j+=1
    args={'tours':tours,'travelers':travelers,'range':range(j)}
    return render(request,'zudipay/fadakpage.html',args)
