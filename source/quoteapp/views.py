from quoteapp.models import Quote
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@ensure_csrf_cookie
def Indexview(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "index.html")

