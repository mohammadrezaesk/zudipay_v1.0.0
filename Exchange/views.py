from django.shortcuts import render
from .models import pricecard
# Create your views here.
def show_prices(request):
    cards = pricecard.objects.order_by('country')
    args={'cards':cards}
    return render(request,'exchange/exchange.html',args)
