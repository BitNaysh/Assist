from django.shortcuts import render
from django.http import HttpResponse
#from chat import chat_model
# Create your views here.

def chat (request):
    return HttpResponse("Hello world!")
