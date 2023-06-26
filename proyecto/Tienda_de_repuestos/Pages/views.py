from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, "Pages/index.html")

def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('message')

        contact = Contact(full_name=name, email=email, phone=phone, msg=msg)
        contact.save()

    return render(request, "Pages/index.html")