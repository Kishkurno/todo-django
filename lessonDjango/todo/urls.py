from django.contrib import admin
from django.urls import path

from .views import TodoView,TodoDetail

urlpatterns = [

    path('todos/',TodoView.as_view()),
    path('todos/<int:pk>/', TodoDetail.as_view()),
]