from django.urls import path 
from danheng.views import index

urlpatterns = [
    path('', index),
]