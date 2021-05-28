from django.contrib import admin
from django.urls import path, include

from quoteapp.views import Indexview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Indexview, name='index'),
    path('', include('api_v1.urls', namespace='api_v1')),
    path('base-auth/', include('rest_framework.urls')),
    path('', include('accounts.urls', namespace='accounts')),
]
