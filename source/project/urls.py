from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from quoteapp.views import Indexview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Indexview, name='index'),
    path('', include('api_v1.urls', namespace='api_v1')),  
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('', include('accounts.urls', namespace='accounts')),
]
 