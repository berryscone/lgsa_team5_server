from django.urls import path

from .views import VehicleDetailView

urlpatterns = [
    path('vehicles/', VehicleDetailView.as_view(), name='vehicle-detail'),
]
