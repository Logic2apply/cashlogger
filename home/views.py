from django.contrib import messages
from home.models import Contact
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def contactUs(request):
    if request.method == 'POST':
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")

            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()

            messages.success(request, "Your Message Submitted Successfully!!")
        except:
            messages.error(request, "Failed to Submit Your Message!! Please check your entered information.")

        redirect("contact")

    return render(request, "home/contact.html")