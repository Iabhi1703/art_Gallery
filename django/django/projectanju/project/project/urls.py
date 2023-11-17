from django.contrib import admin
from django.urls import path, include
from members.views import *

urlpatterns = [
    path('', view, name="view"),
    path('news/', news, name="news"),
    path('news-single/', nes, name="news-single"),
    path('visit/', me, name="visit"),
    path('exhibitions/', you, name="exhibitions"),
    path('exhibition/', qw, name="exhibition-detail"),
    path('collections/', col, name="collections"),
    path('collection-detail/', cold, name="collection-detail"),
    path('about/', ab, name="about"),
    path('contact/', con, name="contact"),
    path('signup/', signup, name="signup"),
    path('user_login/', user_login, name="user_login"),
    path('home/', home, name="home"),
    path('logout/', LogoutPage, name='logout'),
    path('confirmation/', confirmation, name='confirmation'),
    path('confirmation/index.html', view, name='view'),
    path('', include('members.urls')),
    path('vr', vr, name='vr'),
    path('ContactUs/', contactme, name="contact_us"),
    path('newsletter', newsletter, name='newsletter'),
    path('admin/', admin.site.urls),
    path('contact_us', contact_us, name='contact_us'),
    path('themes', themes, name='themes'),
    path('team', team, name='team'),
]
