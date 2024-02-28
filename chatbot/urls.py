from django.urls import path
from . import views
urlpatterns = [
    path('chatbot', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('chatbot.html', views.blog, name='chatbot.html'),
    path('profile', views.profile, name='profile'),
    
]