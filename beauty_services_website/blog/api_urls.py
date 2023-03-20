from django.urls import path
from . import views

#api endpoint

urlpatterns = [
    path('posts', views.api_get_post)
]