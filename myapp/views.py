from django.shortcuts import render

# Create your views here.

def first(requests):
    return render(requests,'first.html')

def second(requests):
    return render(requests,'second.html')

def third(requests):
    return render(requests,'third.html')

def four(requests):
    return render(requests,'four.html')

def five(requests):
    return render(requests,'five.html')
