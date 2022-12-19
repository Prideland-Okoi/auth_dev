from django.urls import path
from . import views

app_name='codelib'

urlpatterns = [
    path('home/', views.homeview, name = 'home'),]