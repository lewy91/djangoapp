from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    return HttpResponse("<h1>Wstawaj samuraju, mamy miasto do spalenia!</h1>")


def komunikat (request):
    return HttpResponse("Chwała Kwiciorowi!!!")


def opcje(request):
    return HttpResponse("Wybierz sobie coś")
