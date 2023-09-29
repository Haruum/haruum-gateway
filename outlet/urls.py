from django.urls import path
from .views import (
    serve_get_outlet_data,
    serve_update_laundry_outlet_data,
    serve_update_item_laundry_outlet_category_provided,
    serve_get_reviews_of_outlet,
)


urlpatterns = [
    path('data/', serve_get_outlet_data),
    path('update/', serve_update_laundry_outlet_data),
    path('update/services-provided/', serve_update_item_laundry_outlet_category_provided),
    path('reviews/', serve_get_reviews_of_outlet),
]
