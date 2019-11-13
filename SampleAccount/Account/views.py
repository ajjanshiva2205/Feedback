from django.shortcuts import render
from .models import Customer_Account

def index(request):
    return render(request,"index.html")

def create(request):
    return render(request,"create.html")

def saveDetails(request):
    number=request.POST.get("acc_no")
    name=request.POST.get("cname")
    balance=request.POST.get("acc_bal")
    password=request.POST.get("pword")

    ca=Customer_Account(idno=number,name=name,balance=balance,password=password)
    ca.save()
    return render(request,"create.html",{"data":"data credited"})

def viewDeatils(request):
    qs=Customer_Account.objects.all()
    return render(request,"view.html",{"data":qs})

def login(request):
    id=request.GET.get("id")
    return render(request,"password.html",{"id":id})

def see(request):
    idno=request.POST.get("id_num")
    cpowrd=request.POST.get("c_pword")
    try:
        data=Customer_Account.objects.get(idno=idno,password=cpowrd)
    except:

        return render(request, "password.html", {"message": "invalid details"})
    if data:
        cdata=Customer_Account.objects.filter(idno=idno)
        return render(request,"result.html",{"cdata":cdata})
    else:
        return render(request,"password.html",{"message":"invalid details"})
