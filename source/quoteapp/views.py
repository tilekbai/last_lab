from django.shortcuts import render

# Create your views here.

def Indexview(request):
    return render(request, 'index.html')