from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import helloWorld, home, post, category, about, search_results, register

urlpatterns = [
    path('hello/', helloWorld),
    path('home/', home),
    path('/', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>', category),
    path('about/', about),
    path('search/', search_results, name='search_results'),
    path('register/', register)
]
