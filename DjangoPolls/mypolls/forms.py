from django.forms import ModelForm
from .models import Poll, PollChoice
from django import forms


class PollForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, required=True)
    description = forms.CharField(label='Description', max_length=255, required=False, widget=forms.Textarea)
    firstChoice = forms.CharField(label='First choice', max_length=100, required=True)
    secondChoice = forms.CharField(label='Second choice', max_length=100, required=True)
    winVote = forms.IntegerField(label='How much votes for win needed', required=False)

    def create_poll(self, data):
        poll = Poll()
        poll.title = data['title']
        poll.description = data['description']
        poll.winVote = data['winVote']

        fc = PollChoice()
        fc.value = data['firstChoice']
        fc.votes = 0
        fc.save()

        poll.firstChoice = fc

        sc = PollChoice()
        sc.value = data['secondChoice']
        
        sc.votes = 0
        sc.save()

        poll.secondChoice = sc

        poll.save()