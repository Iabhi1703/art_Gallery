from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()
class BookingEvent(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    art_genre = models.CharField(max_length=100)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking on {self.booking_date}"
    
class NewsletterSubscriber(models.Model):
    email = models.CharField(max_length=100)