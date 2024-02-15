# item_tracker_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),  # Include the items app URLs under the 'api/' prefix
]
