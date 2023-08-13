from django.urls import path
from .views import (
    serve_get_outlets,
    serve_get_laundry_outlet_data,
    serve_get_outlet_services
)


urlpatterns = [
    path('outlets/', serve_get_outlets),
    path('outlet/details/', serve_get_laundry_outlet_data),
    path('outlet/services/', serve_get_outlet_services),
]
