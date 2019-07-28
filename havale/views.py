from django.shortcuts import render

# Create your views here.
def havaleform(request):
    args = {}
    return render(request,'havale/havaleform.html',args)
def payform(request,company,az,be,count,day,month):
    args = {'count':range(count),'company':company,'to':be,'from':az,'day':day,'month':month}
    return render(request,'havale/payform.html',args)
