from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import smtplib

def home_page(request):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sridhar200288@gmail.com", "mhcd uzlb zgsa uiwq")
        message = f"hello"
        s.sendmail("sridhar200288@gmail.com", 'sridhar200288@gmail.com', message)
        s.quit()
        print( 'Email sent!')
        return render(request,'index.html')

@csrf_exempt
def form_page(request):

    if request.method == "POST":
        save_data = class_form(request.POST)
        save_data.save()
    context ={
        'add_variable':class_form
    }
    return render(request,'form.html',context)

def view_page(request):
    context = {
        'view_data': class_model.objects.all()
    }
    return render(request,'view.html',context)

def delete_data(request,id):
    select_data =class_model.objects.get(id=id)
    select_data.delete()
    return redirect('/view/')




def update_data(request,id):
    select_data = class_model.objects.get(id=id)
    if request.method =="POST":
        update_variable = class_form(request.POST,instance=select_data)
        update_variable.save()
        return redirect('/view/')
    context = {
        'add_variable': class_form(instance=select_data) 
    }
    return render(request,'update.html',context)
        
def http(request):
    return HttpResponse('<h1>sridhar<h1>')