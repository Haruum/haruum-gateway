from django.urls import path
from .views import serve_get_customer_data, serve_update_customer_address


urlpatterns = [
    path('data/', serve_get_customer_data),
    path('update-address/', serve_update_customer_address),
]
