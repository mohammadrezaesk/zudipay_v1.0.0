from django.shortcuts import render , redirect
from Exchange.models import pricecard
from .forms import UpdatePrices
from .models import adminpaneluser

# Create your views here.
def changecard (request):
    cards = pricecard.objects.order_by('country')
    if request.method=="GET":
        args={'cards':cards}
        return render(request,"zudipayadmin/changecard.html",args)
    else:
        for card in cards:
            newprice=request.POST[card.city]
            card.price=newprice
            card.save()
        return redirect('zudipayadmin:changecard')
def login(request):
    users = adminpaneluser.objects.order_by('username')
    if request.method=="GET":
        args={'uesrs':users}
        return render(request,"zudipayadmin/login.html",args)
    else:
        usernamee = request.POST['username']
        passworde = request.POST['password']
        for userx in users:
            if userx.username == usernamee and userx.password==passworde:
                return redirect('zudipayadmin:changecard')
        return redirect('zudipayadmin:login')
