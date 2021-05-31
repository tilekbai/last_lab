from django.http import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import *
# Create your views here.


class QuoteCreateView(generics.CreateAPIView):
    serializer_class = QuoteDetailSerializer

    
class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteDetailSerializer
    queryset = Quote.objects.all()

    
class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteListSerializer
    queryset = Quote.objects.all()
    # response = response.HttpResponse(queryset)