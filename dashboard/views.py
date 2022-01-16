from django.shortcuts import redirect, render
from django.http import HttpResponse
from dashboard.models import Ledger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cashlogger.encryption_utils import encrypt, decrypt


# Create your views here.
@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required
def ledger(request):
    if request.method == "POST":
        try:
            username = request.user
            date = request.POST.get("date")
            name = request.POST.get("name")
            debitCredit = request.POST.get("debitCredit")
            particular = request.POST.get("particular")
            amount = request.POST.get("amount")

            ledger = Ledger(username=username, date=date, name=name, debitCredit=debitCredit, particular=particular, amount=amount)
            ledger.save()

        except Exception as e:
            messages.error(request, "An error occured while trying to make entry in ledger. Please try again!")

    return redirect("dashboard")



@login_required
def debitCredit(request, debitCredit):
    username = request.user
    data = Ledger.objects.filter(debitCredit=debitCredit.lower(), username=username)

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

        # encrypt th sno
        encryptedKeyData = {}
        for data in data_by_date:
            encrypted_sno = encrypt(data.sno)
            encryptedKeyData.update({data:encrypted_sno})

        date_partitioned.update({date : encryptedKeyData})

   
    dataset = {
        "dataset": date_partitioned,
        "debitCredit": debitCredit,
        "isNewestSelected": (sort=="NewestFirst" or sort==None)
    }
    return render(request, "dashboard/debitCredit.html", dataset)


@login_required
def delete_BySNO(request, sno):
    # Decrypt the serial No (SNO)
    decrypted_sno = decrypt(sno)

    # Get Username and encrypt
    username = request.user
    ledger = Ledger.objects.filter(sno = decrypted_sno, username=username)

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


@login_required
def viewEntry(request, sno):
    # Get user and decrypt the sno
    username = request.user
    decrypt_sno = decrypt(sno)

    # Change the entry
    if request.method == 'POST':
        date = request.POST.get("date")
        name = request.POST.get("name")
        debitCredit = request.POST.get("debitCredit")
        particular = request.POST.get("particular")
        amount = request.POST.get("amount")
        redirectTo = request.POST.get("redirect")

        ledger = Ledger.objects.filter(sno=decrypt_sno, username=username)[0]

        ledger.date = date
        ledger.name = name
        ledger.debitCredit = debitCredit
        ledger.particular = particular
        ledger.amount = amount

        ledger.save()
        messages.success(request, 'Your Entry Updated Successfully.')
        return redirect(redirectTo)


    # Redirector
    if request.method == "GET":
        redirector = request.GET.get("redirect")
        if redirector is not None:
            str(redirector).upper()
            redirectTo = f"/dashboard/Ledger/{redirector}/"
        else:
            redirectTo = "/" # WHICH WILL BE DASHBOARD


    ledger = Ledger.objects.filter(sno = decrypt_sno, username = username)[0]
    if ledger is not None:
        data = {
            "entry" : ledger,
            "encrypt_sno" : sno,
            "decrypt_sno" : decrypt_sno,
            "redirect_to" : redirectTo
        }
        return render(request, 'dashboard/update.html', data)