from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_display_view, name='home-page')
]