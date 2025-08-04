from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('403/', views.forbidden, name='403'),
]