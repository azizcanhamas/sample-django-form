from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def home(request):
    if request.method=="GET":
        form=ContactForm(request.GET)
        if form.is_valid():
            form.save()
            form=ContactForm()
    else:
        form=ContactForm()

    context={
        'form':form
    }

    return render(request,"home/index.html",context)