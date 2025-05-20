from django.db import models

# Create your models here.
class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, help_text="First name of the record holder")
    last_name = models.CharField(max_length=50, help_text="Last name of the record holder")
    email = models.EmailField(max_length=100, unique=True, help_text="Email address of the record holder (must be unique)")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Phone number of the record holder (e.g., +91-XXXXXXXXXX)")
    address = models.CharField(max_length=255, blank=True, help_text="Full address of the record holder")
    city = models.CharField(max_length=100, blank=True, help_text="City of the record holder")
    state = models.CharField(max_length=100, blank=True, help_text="State or province of the record holder")
    pincode = models.CharField(max_length=10, blank=True, help_text="Pincode or Zip code of the record holder")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"