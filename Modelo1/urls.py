from django.contrib import admin
from django.urls import path
from Modelo1.views import return_page, example, example2

urlpatterns = [
    path('', return_page, name="home"),
    path('wilie/', example, name="example"),
    path('wilie2/', example2, name="example2"),
]
