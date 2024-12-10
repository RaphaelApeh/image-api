from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'api'

urlpatterns = [
    path('v1/', views.list_all_image_view, name='api-list'),
    path('token/', obtain_auth_token)
]