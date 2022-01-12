from django.contrib import messages
# from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

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
                messages.success(request, "New User Created Successfully!! Login to start making records.")
                return redirect("signIn")
            else:
                messages.error(request, "User couldn't be created, please check your passwords!!")
                return redirect("signUp")

        return render(request, "authenticate/signUp.html")
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
                return redirect("signIn")
        return render(request, "authenticate/signIn.html")
    
    else:
        return redirect("/")


@login_required
def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Successful.")
    return redirect("/")