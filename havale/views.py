from django.shortcuts import render

# Create your views here.
def havaleform(request):
    args = {}
    return render(request,'havale/havaleform.html',args)
