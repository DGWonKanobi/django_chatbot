from django.shortcuts import render, redirect
from django.http import JsonResponse
from openai import OpenAI
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone
from dotenv import load_dotenv
import os
load_dotenv()
OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
# openai_api_key = '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'
client = OpenAI(api_key=OPEN_AI_KEY)


def ask_openai(message):
    response = client.chat.completions.create(
    model = "gpt-4",
    messages=[
       {"role": "system", "content": "You are a helpful assistant."},
       {"role": "user", "content": message},
    ]
)
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.

def home(request):
   return render(request, 'home.html', {})

def blog(request):
   return render(request, 'blog.html', {})

def profile(request):
   return render(request, 'profile.html', {})

def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
      message = request.POST.get('message')
      response = ask_openai(message)

      chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
      chat.save()
      return JsonResponse({'message': message, 'response': response })
    return render(request, 'chatbot.html', {'chats': chats})

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(request, username=username, password=password)
      if user is not None:
         auth.login(request, user)
         return redirect('blog')
      else:
         error_message = 'Invalid username or password'
         return render(request, 'login.html', {'error_message': error_message})
   else:
        return render(request, 'login.html')

def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password1 = request.POST['password1']
      password2 = request.POST['password2']

      if password1 == password2:
        try:
             user = User.objects.create_user(username, email, password1)
             user.save()
             auth.login(request, user)
             return redirect('chatbot')
        except:
           error_message = 'Error Creating Your Account'
           return render(request, 'register.html', {'error_message': error_message})
      else:
          error_message = 'Passwords Do Not Match'
          return render(request, 'register.html', {'error_message': error_message})
   return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('login')