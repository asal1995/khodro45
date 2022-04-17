
from django.db import models

from User.models import Bider, Customer


class Brand(models.Model):
    title = models.CharField(max_length=50, verbose_name="brand")

    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Appointment(models.Model):

    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name="brand")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer"
    )
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.customer.username}"


class Inspection(models.Model):
    INS_STATUS = [("Under inspection", "Under inspection"), ("inspected", "inspected")]
    status = models.CharField(max_length=50, choices=INS_STATUS, verbose_name="status")

    appointmet = models.ForeignKey(
        "Appointment", on_delete=models.CASCADE, related_name="appointment"
    )
    
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status}"


class Bid(models.Model):

    bider = models.ForeignKey(Bider, on_delete=models.CASCADE, related_name="bider")
   
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bider}"


class Auction(models.Model):
    start_price = models.PositiveBigIntegerField()

    inspection = models.ForeignKey("Inspection", on_delete=models.CASCADE)
    bider = models.ForeignKey("Bid", on_delete=models.CASCADE, related_name="winner")

    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bider}  with The final price:{self.start_price}"

