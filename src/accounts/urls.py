from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.user_creation_view, name='account-signup')    
]