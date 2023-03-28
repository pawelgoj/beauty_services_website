from django.urls import path
from . import views

app_name = "business"

urlpatterns = [
    path('omnie/', views.about_me, name="about_me"),
    path('social_data/', views.social_data, name="social_data"),
    path('price_list/', views.price_list, name="price_list"),
    path('', views.index, name='index')
]