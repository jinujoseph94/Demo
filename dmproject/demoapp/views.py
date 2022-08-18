from django.http import HttpResponse
from django.shortcuts import render
from .models import Team


# Create your views here.
def demo(request):
    obj = Team.objects.all()
    return render(request, "index.html", {'result': obj})
