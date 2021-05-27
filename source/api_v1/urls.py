from django.urls import path

from .views import QuoteCreateView, QuoteDetailView, QuoteListView

app_name = 'api_v1'

urlpatterns = [
    path('quote/create/', QuoteCreateView.as_view(), name='create-quote'),
    path('quote/detail/<int:pk>/', QuoteDetailView.as_view(), name='detail-quote'),
    path('quote/list/', QuoteListView.as_view(), name='list-quote'),
]
