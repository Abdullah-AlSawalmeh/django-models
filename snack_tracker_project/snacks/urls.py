from snacks.models import Snack
from django.contrib import admin
from django.urls import path, include
from .views import Index, SnackListView, SnackDetailView

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('snacks/',SnackListView.as_view(),name='snacks_list'),
    path('snacks/<int:pk>', SnackDetailView.as_view(), name='snack_details'),
]
