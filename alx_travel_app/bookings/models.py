# bookings/models.py
"""
Models for the bookings app
"""
from django.db import models
from listings.models import Listing
from users.models import User

class BookingStatus(models.TextChoices):
    """
    Booking status choices
    """
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'
    PENDING_PAYMENT = 'pending_payment'
    PAID = 'paid'
    REFUNDED = 'refunded'
    EXPIRED = 'expired'
    CANCELLED_BY_USER = 'cancelled_by_user'

class Booking(models.Model):
    """
    Booking model
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=BookingStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.listing.title}"