from django.contrib import messages
from django.http.response import Http404
from home.models import Contact
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

        return redirect("contact")

    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")


def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            pass1 = request.POST.get("pass1")
            pass2 = request.POST.get("pass2")

            if pass1==pass2:
                newUser = User.objects.create_user(username, email, pass1)
                newUser.first_name = firstname
                newUser.last_name = lastname

                newUser.save()
                messages.success(request, "New User Created Successfully!!")
                return redirect("home")
            else:
                messages.error(request, "User couldn't be created, please check your passwords!!")
                return redirect("signUp")

        return render(request, "home/signUp.html")
    else:
        return redirect("/")


def signIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            signInUsername = request.POST.get("signInUsername")
            signInPassword = request.POST.get("signInPassword")

            user = authenticate(username=signInUsername, password=signInPassword)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfull!!")
                return redirect("/")
            else:
                messages.error(request, "Please check your username and Password and try again.")
                return redirect("/sign-in/")
        return render(request, "home/signIn.html")
    
    else:
        return redirect("/")


@login_required(redirect_field_name="signIn")
def handleLogout(request):
    if User.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successful.")
        return redirect("/")

    else:
        return Http404