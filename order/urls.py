from django.urls import path
from .views import (
    serve_create_order,
    serve_get_laundry_orders_of_outlet,
    serve_get_laundry_progress_statuses,
    serve_update_laundry_progress_status,
    serve_get_active_laundry_orders_of_a_customer,
    serve_get_completed_laundry_orders_of_a_customer,
    serve_get_customer_order_details,
    serve_submit_rating_for_laundry_order,
)


urlpatterns = [
    path('create/', serve_create_order),
    path('outlet/', serve_get_laundry_orders_of_outlet),
    path('status/all/', serve_get_laundry_progress_statuses),
    path('status/update/', serve_update_laundry_progress_status),
    path('customer/active/', serve_get_active_laundry_orders_of_a_customer),
    path('customer/completed/', serve_get_completed_laundry_orders_of_a_customer),
    path('customer/detail/', serve_get_customer_order_details),
    path('review/submit/', serve_submit_rating_for_laundry_order),
]
