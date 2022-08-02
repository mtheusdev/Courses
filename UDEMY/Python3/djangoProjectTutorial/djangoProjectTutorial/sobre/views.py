from django.shortcuts import render

# Create your views here.

def metodoSobre(request):
    return render(request, 'sobre/bla.html')