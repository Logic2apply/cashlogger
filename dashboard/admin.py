from django.contrib import admin
from dashboard.models import Ledger, LedgerAdmin

# Register your models here.
admin.site.register(
    Ledger,
    LedgerAdmin
)