from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_word(request):
    return HttpResponse('Hello django app')

