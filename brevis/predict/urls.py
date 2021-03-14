from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predictor/', views.call_model.as_view(), name="call_model"),
]