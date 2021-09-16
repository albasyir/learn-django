from django.urls import path
from . import views

# URL Patterns
urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
