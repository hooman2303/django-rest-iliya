from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Contact_Form
# Create your views here.
def index(req):
    return render(req, 'index.html')


def contact(req):
    if req.method == "POST":
        form = Contact_Form(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"your form is successfully added" )
        form = Contact_Form()
        return render(req, 'index.html',  {'form':form})
        
    else:
        form = Contact_Form()


    
    
    return render(req, 'contact.html', {'form':form})