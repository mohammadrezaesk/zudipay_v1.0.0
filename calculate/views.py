from django.shortcuts import render
from Exchange.models import pricecard
# Create your views here.
def calculator(request):

    dot = pricecard.objects.get(city="طهران",type="100dollar").price
    dot *= 10
    dit = pricecard.objects.get(city="نقدا",type="1000dinar").price
    tdo = dot
    tdi = dit
    args = {'convertrate':[dot,dit,tdo,tdi]}
    return render(request,"calculator/calculator.html",args)
