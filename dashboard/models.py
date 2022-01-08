from django.db import models
from django.contrib import admin

# Create your models here.
class Ledger(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256, null=False)
    date = models.DateField()
    name = models.CharField(max_length=50)
    debitCredit = models.CharField(max_length=15)
    particular = models.CharField(max_length=300)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.username} {self.debitCredit}ed {self.amount} on {self.date}"


class LedgerAdmin(admin.ModelAdmin):
    list_display = (
        "sno",
        "username",
        "date",
        "name",
        "particular",
        "amount"
    )
