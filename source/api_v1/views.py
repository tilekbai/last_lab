from django.shortcuts import render
from rest_framework import generics

from .serializers import *
# Create your views here.


class QuoteCreateView(generics.CreateAPIView):
    serializer_class = QuoteDetailSerializer

    
class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteDetailSerializer
    queryset = Quote.objects.all()