from django.db import models
# Create your models here.
class PollChoice(models.Model):
    value = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.value

class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    firstChoice = models.ForeignKey(PollChoice, related_name='firstChoice', on_delete=models.PROTECT)
    secondChoice = models.ForeignKey(PollChoice, related_name='secondChoice', on_delete=models.PROTECT)  
    winVote = models.IntegerField(default=50)

    def __str__(self):
        return self.title