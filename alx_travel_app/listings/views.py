from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from bookings.models import Booking
from .models import Listing
from django.conf import settings
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import logging

from .serializers import (
    ListingSerializer,
    BookingSerializer,
)

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing Listing
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing Bookings
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    


