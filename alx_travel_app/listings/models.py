# listings/models.py
"""
Models for the listings app
"""
from django.db import models

class ListingStatus(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SOLD = 'sold'
    RENTED = 'rented'

# Create your models here.
class Listing(models.Model):
    """
    Model for a listing
    """
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.IntegerField(null=False, blank=False)
    addresses = models.ForeignKey('addresses.Address', on_delete=models.CASCADE)
    bedrooms = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=100, choices=ListingStatus.choices, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
