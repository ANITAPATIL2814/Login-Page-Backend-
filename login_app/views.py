from django.shortcuts import render,HttpResponse,redirect
from .models import LoginPage
# Create your views here.
def Create(request):
    if request.method=="POST":
        n=request.POST['uname']
        mail=request.POST['uemail']
        password=request.POST['upass']
        a=LoginPage.objects.create(name=n,email=mail,password=password)
        a.save()
        # return HttpResponse("data is inserted")
        return redirect('/dashboard')
    else:
        print("request is:",request.method)
        return render(request,'login.html') 
    
def dashboard(request):
    #to display record
    a=LoginPage.objects.all()
    context={}
    context['data']=a #data save in dictionary
    return render(request,"dashboard.html",context) 

def edit(request,rid):
    if request.method=='POST':
        # update new data
        n=request.POST['uname']
        mail=request.POST['uemail']
        password=request.POST['upass']
        a=LoginPage.objects.filter(id=rid)
        a.update(name=n,email=mail,password=password) 
        return redirect('/dashboard')
    else:
        a=LoginPage.objects.get(id=rid)
        context={}
        context['data']=a
        return render(request, 'edit.html',context)
def delete(request,rid):
    # print("id of record  to be deleted :",rid)
    a=LoginPage.objects.filter(id=rid)
    a.delete()
    return redirect('/dashboard')

def google_login(request):
    # Redirect users to Google.html
    return render(request, 'google.html')