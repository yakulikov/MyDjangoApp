from django.shortcuts import render
from rest_framework.views import APIView
from mypolls.models import Poll
from rest_framework.response import Response
import random
from django.views.decorators.csrf import csrf_exempt

class GetPollinfo(APIView):
    def get(self, request):
        pollid = request.GET.get("id") #request 
        if Poll.objects.filter(id=pollid).exists():
            pollObj = Poll.objects.get(id=pollid)
            return Response({
                "ok": True,
                "title": pollObj.title,
                "description": pollObj.description
            })
        else:
            return Response({
                "ok": False,
                "verbose": "no poll with this id"
            })

class GetMathEquation(APIView):
    def get(self, request):
        equation = ''
        number_of_asterisks = 0
        for i in range(random.randint(3, 5)):
            r = random.randint(1, 3)
            if r == 1:
                symbol = '-'
            elif r == 2:
                 symbol = '+'
            elif number_of_asterisks < 3:
                symbol = '*'
                number_of_asterisks += 1
            else:
                i -= 1
            equation += str(random.randint(2, 10)) + symbol

        equation = equation[:len(equation) - 1]
        result = eval(equation)

        return Response({
                "equation": equation,
                "result": result
            })

class SetPollVote(APIView):

    @csrf_exempt
    def post(self, request):
        pollId = request.POST.get("pollId")
        answerId = request.POST.get("answerId")
        pollObj = Poll.objects.get(id=pollId)

        if answerId == "0":
            pollObj.firstChoice.votes += 1
            pollObj.firstChoice.save()
        else:
            pollObj.secondChoice.votes += 1
            pollObj.secondChoice.save()
        
        return Response({"ok": True})

class GetPollVotes(APIView):
    def get(self, request):
        pollid = request.GET.get("pollid")
        if Poll.objects.filter(id=pollid).exists():
            pollObj = Poll.objects.get(id=pollid)

            return Response({
                    "firstVote": pollObj.firstChoice.votes,
                    "secondVote": pollObj.secondChoice.votes,
                    "winVote": pollObj.winVote
                })
        else:
            return Response({
                "ok": False
            })