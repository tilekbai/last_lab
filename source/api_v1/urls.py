from django.urls import path

from .views import QuoteCreateView

app_name = 'api_v1'

urlpatterns = [
    path('quote/create/', QuoteCreateView.as_view(), name='create-quote'),
]
