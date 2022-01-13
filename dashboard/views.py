from django.shortcuts import redirect, render
from django.http import HttpResponse
from dashboard.models import Ledger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import hashlib


# Create your views here.
@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required
def ledger(request):
    if request.method == "POST":
        try:
            username = request.user.username
            username_enc = hashlib.sha256(username.encode('utf-8')).hexdigest()
            date = request.POST.get("date")
            name = request.POST.get("name")
            debitCredit = request.POST.get("debitCredit")
            particular = request.POST.get("particular")
            amount = request.POST.get("amount")

            ledger = Ledger(username=username_enc, date=date, name=name, debitCredit=debitCredit, particular=particular, amount=amount)
            ledger.save()

        except Exception as e:
            messages.error(request, "An error occured while trying to make entry in ledger. Please try again!")

    return redirect("dashboard")



@login_required
def debitCredit(request, debitCredit):
    username = request.user.username
    username_enc = hashlib.sha256(username.encode('utf-8')).hexdigest()
    data = Ledger.objects.filter(debitCredit=debitCredit.lower(), username=username_enc)

    # TODO: Pending Search By date
    searchByDate = request.GET.get("date")
    sort = request.GET.get("sort")


    if sort == 'NewestFirst' or sort==None:
        datedata = data.order_by("-date")
        dates = sorted({date.date for date in datedata}, reverse=True)
    elif sort=='OldestFirst':
        datedata = data.order_by("date")
        dates = sorted({date.date for date in datedata}, reverse=False)

    date_partitioned = {}
    for date in dates:
        data_by_date = datedata.filter(date=date)
        date_partitioned.update({date : data_by_date})
    
   
    dataset = {
        "dataset": date_partitioned,
        "debitCredit": debitCredit,
        "isNewestSelected": (sort=="NewestFirst" or sort==None)
    }
    return render(request, "dashboard/debitCredit.html", dataset)


@login_required
def delete_BySNO(request, sno):
    # Get Username and encrypt
    username = request.user.username
    username_enc = hashlib.sha256(username.encode('utf-8')).hexdigest()
    ledger = Ledger.objects.filter(sno = sno, username=username_enc)

    if request.method == "GET":
        redirector = request.GET.get("redirect")
        if redirector is not None:
            str(redirector).upper()
            redirectTo = f"/dashboard/Ledger/{redirector}/"
        else:
            redirectTo = "/" # WHICH WILL BE DASHBOARD
        
    if ledger is not None:
        ledger.delete()
        messages.success(request, "Successfully deleted the required entry.")
        return redirect(f"{redirectTo}")
    else:
        messages.error(request, "Can't delete the required entry please try again..!")
        return redirect(f"{redirectTo}")