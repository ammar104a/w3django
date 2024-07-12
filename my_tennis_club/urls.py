from django.contrib import admin
from django.urls import path, include
# my_tennis_club/my_tennis_club/urls.py
urlpatterns = [
    path('', include('members.urls')),  # Include the members.urls here
    path('admin/', admin.site.urls),
]
