from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import ContactUs
from members.form import MyForm
from .models import BookingEvent
from members.models import BookingEvent
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse
from .models import NewsletterSubscriber
from django.contrib.auth.decorators import login_required


def view(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def nes(request):
    return render(request, 'news-single.html')

def me(request):
    return render(request, 'visit.html')

def you(request):
    return render(request, 'exhibitions.html')

def qw(request):
    return render(request, 'exhibition-detail.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')



        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # Use the create_user method to create a new user
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect("user_login")

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("OOPS! <br> Your username or password is incorrect!")
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('user_login')


@login_required
def col(request):
    return render(request, 'collections.html')

def cold(request):
    return render(request, 'collection-detail.html')

def ab(request):
    return render(request, 'about.html')

def con(request):
    return render(request, 'contact.html')


def contactme(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')

        contact = ContactUs(name=name, email=email, phone_number=phone_number, message=message)
        contact.save()

    return redirect("view")

def book_event(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            art_genre = form.cleaned_data['art_genre']
            booking_date = form.cleaned_data['booking_date']

            booking = BookingEvent(name=name, email=email, art_genre=art_genre, booking_date=booking_date)
            booking.save()

            return redirect('confirmation')

    else:
        form = MyForm()

    return render(request, 'booking_form.html', {'form': form})


def view_booking(request, booking_id):
    try:
        booking = BookingEvent.objects.get(id=booking_id)
        return render(request, 'booking_detail.html')
    except BookingEvent.DoesNotExist:
        return render(request, 'booking_not_found.html', {'BookingEvent': BookingEvent})

#

def new(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            art_genre = form.cleaned_data['art_genre']
            booking_date = form.cleaned_data['booking_date']

            booking = BookingEvent(name=name, email=email, art_genre=art_genre, booking_date=booking_date)
            booking.save()

            subject = "email confirmation"
            mess = "Thanks for connecting with us"
            email_from = settings.EMAIL_HOST_USER
            email_message = EmailMessage(subject, mess, email_from, [email])
            email_message.send()

            return redirect('confirmation')
    else:
        form = MyForm()

    return render(request, 'new.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')

def vr(request):
    return render(request, 'vr.html')

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriber(request.POST)  
        if form.is_valid():
            email = form.cleaned_data['email']

            subscriber = NewsletterSubscriber(email=email)  
            subscriber.save()

            subject = "Email Confirmation"
            message = "Thanks for connecting with us"
            email_from = settings.EMAIL_HOST_USER
            email_message = EmailMessage(subject, message, email_from, [email])
            email_message.send()

            return redirect('confirmation')
    else:
        form = NewsletterSubscriber()  

    return render(request, 'newsletter.html', {'form': form})

def contact_us(request):
    return render(request, 'newsletter.html')

def themes(request):
    return render (request,'themes.html')

def team(request):
    return render (request,'team.html')
