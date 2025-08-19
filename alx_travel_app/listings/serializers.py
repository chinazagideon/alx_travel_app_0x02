# listings/serializers.py
"""
Serializers for the listings app
"""
from rest_framework import serializers
from .models import Listing
from bookings.models import Booking
from users.serializers import UserDetailSerializer
from addresses.serializers import AddressDetailSerializer
from reviews.serializers import ReviewDetailSerializer

field_list = [
    'id',
    'title',
    'description',
    'price',
    'bedrooms',
    'owner', # UserDetailSerializer
    'addresses', # AddressDetailSerializer
    'status',
    'reviews', # ReviewDetailSerializer
    'created_at',
]
class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the listing
    """
    reviews = ReviewDetailSerializer(many=True, read_only=True)
    reviews_count = serializers.SerializerMethodField(read_only=True)

    def get_reviews_count(self, obj):
        """
        Get the number of reviews for the listing
        """
        return obj.reviews.count()
    
    
    class Meta:
        model = Listing
        read_only_fields = ['reviews', 'reviews_count']
        fields = [*field_list, 'reviews', 'reviews_count']

class ListingBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the listing booking
    """
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in', 'check_out', 'status']
class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the booking
    """
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in', 'check_out', 'status']

class ListingDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the listing detail
    """
    owner = UserDetailSerializer(read_only=True)
    address = AddressDetailSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = field_list
        depth = 1
        read_only_fields = ['reviews', 'reviews_count']