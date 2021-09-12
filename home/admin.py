from django.contrib import admin
from home.models import Contact

# Admin Customizations
@admin.action(description="Mark Selected as Resolved")
def make_selected_resolved(modeladmin, request, queryset):
    queryset.update(resolved = True)

@admin.action(description="Mark Selected as Unresolved Contacts")
def make_selected_unresolved(modeladmin, request, queryset):
    queryset.update(resolved = False)

# Contact Page customisation
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "message",
        "dateAdded",
        "resolved"
    )

    list_filter = (
        "resolved",
    )

    actions = (
        make_selected_resolved,
        make_selected_unresolved
    )




# Register your models here.
admin.site.register(
    Contact,
    ContactAdmin
)