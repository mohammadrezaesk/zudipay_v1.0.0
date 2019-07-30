from django.shortcuts import render , redirect
from .models import tour , traveler

# Create your views here.
def havaleform(request):
    args = {}
    return render(request,'havale/havaleform.html',args)
def payform(request,company,az,be,count,day,month):
    args = {'count':range(count),'company':company,'to':be,'from':az,'day':day,'month':month}
    if request.method == "GET":
        return render(request,'havale/payform.html',args)
    else:
        tourleader = request.POST['tourleader']
        phone = request.POST['phone']
        enteredtour = tour(tourleader=tourleader, origin=az, destination=be,day=day,month=month,company=company,phone=phone,count=count)
        enteredtour.save()
        for i in range(count):
            newi = str(i)
            firstname = request.POST['firstname'+newi]
            lastname = request.POST['lastname'+newi]
            birthday = request.POST['birthday'+newi]
            birthmonth = request.POST['birthmonth'+newi]
            birthyear = request.POST['birthyear'+newi]
            passport = request.POST['passport'+newi]
            gender = request.POST['gender'+newi]
            ischild = request.POST['ischild'+newi]
            enteredtraveler = traveler(touri = enteredtour , firstname = firstname , lastname = lastname , birthday = birthday , birthmonth = birthmonth , birthyear = birthyear , passport = passport , gender = gender , ischild = ischild)
            enteredtraveler.save()
        return redirect('/pay/success')
def success(request):
    args = {}
    return render(request,'havale/success.html',args)
