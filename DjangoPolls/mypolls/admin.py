from django.contrib import admin

# Register your models here.
from .models import PollChoice, Poll
admin.site.register(Poll)
admin.site.register(PollChoice)
