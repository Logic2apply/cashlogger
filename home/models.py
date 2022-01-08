from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.IntegerField(null=False)
    message = models.CharField(max_length=500, null=False)
    dateAdded = models.DateField(default=now)

    resolved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.message[:100]}... by {self.name} on {self.dateAdded}"
