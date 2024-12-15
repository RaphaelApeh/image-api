from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login_view, name='account-signup')    
]