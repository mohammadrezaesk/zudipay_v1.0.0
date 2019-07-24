from django.shortcuts import render
def home(request):
    args={}
    return render(request,'zudipay/home.html',args)
def about(request):
    args={}
    return render(request,'zudipay/about.html',args)
