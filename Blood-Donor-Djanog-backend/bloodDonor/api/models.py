from django.db import models


class BloodDonor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    blood_type = models.CharField(max_length=3)
    last_donation_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True,)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default="Lahore")