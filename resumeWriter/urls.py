from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.view_name, name="view_name"),
]
