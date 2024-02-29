from django.urls import path
from . import views
from theblog.views import HomeView , ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
urlpatterns = [
    path('chatbot', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('chatbot.html', views.blog, name='chatbot.html'),
    path('/theblog/article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('/theblog/add_post/', AddPostView.as_view(), name='add_post'),
    path('theblog/article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('theblog/article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post')
]