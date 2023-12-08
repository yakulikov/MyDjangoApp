"""
URL configuration for DjangoPolls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mypolls.views import index, LoginPage, PollsMaker, contacts, RegisterPage
from api.views import GetPollinfo, GetMathEquation, SetPollVote, GetPollVotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='mainPage'),
    path('contacts/', contacts, name='contacts'),
    path('PollsMaker/', PollsMaker, name='PollsMaker'),
    path('api/poll/', GetPollinfo.as_view(), name='api_get_all_info'),
    path('api/maths/', GetMathEquation.as_view(), name='api_get_maths'),
    path('api/poll/vote/', SetPollVote.as_view(), name='api_set_vote_for_poll'),
    path('api/poll/get/', GetPollVotes.as_view(), name='api_get_vote_from_poll'),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
]
