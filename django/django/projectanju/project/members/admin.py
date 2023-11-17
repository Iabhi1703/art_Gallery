from django.contrib import admin
from .models import ContactUs


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message')


admin.site.register(ContactUs, ContactUsAdmin)

