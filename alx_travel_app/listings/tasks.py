from config_celery import app

from .models import Payment
from django.core.mail import send_mail
from django.conf import settings


@app.task
def send_booking_email_notification(booking_reference, email_address):
    """
    Send a booking email notification
    """
    subject = f'Booking Confirmation for Reference: {booking_reference}'
    message = f'Hello! Your booking with reference {booking_reference} has been successfully paid. We look forward to seeing you!'
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [email_address])
    
    return "Email sent successfully"