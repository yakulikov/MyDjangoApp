from django.shortcuts import render
import random 
from .models import Poll
from .forms import PollForm
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    if request.method == "POST":
        f = PollForm(request.POST or nothing)
        if f.is_valid():
            f.create_poll(f.data)

            token = "5803321421:AAF-xxzpQ3KFLTzDPLLFJwhfSV_mqnM_UlI"
            chatId = "5006077081"
            url = f'https://api.telegram.org/bot{token}/sendMessage'
            data = {
                'chat_id': chatId,
                    'text': f'title: {f.data["title"]}, description: {f.data["description"]}, first choice: {f.data["firstChoice"]}, second choice: {f.data["secondChoice"]}'
            }
            response = requests.post(url, data=data)


    context = {}
    allPolls = list(Poll.objects.all())
    context['allPolls'] = allPolls
    context['PollForm'] = PollForm()

    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contacts.html', {})

@login_required(login_url='login')
def PollsMaker(request):
    context = {}
    context['PollForm'] = PollForm()

    if request.method == "POST":
        f = PollForm(request.POST or nothing)
        if f.is_valid():
            f.create_poll(f.data)

    return render(request, 'PollsMaker.html', context)

class LoginPage(LoginView):
    template_name = 'login.html'

class RegisterPage(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
