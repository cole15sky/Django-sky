from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.home_urls')),
    path('about/', include('about.urls')),
    path('blogs/', include('blogs.urls')),
]
