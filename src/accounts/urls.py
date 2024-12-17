from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login_view, name='account-login'),
    
    path('signup/', views.user_creation_view, name="accounts-signup")    
]