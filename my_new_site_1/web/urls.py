from django.urls import path
from . import views

app_name = "wed"
urlpatterns = [
    path('', views.web_index),
    path('about', views.about)
]