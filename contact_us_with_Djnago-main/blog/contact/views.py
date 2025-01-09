from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Your message has been successfully sent")

    return render(request, 'contact.html')
