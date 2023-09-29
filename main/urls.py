from django.urls import path
from .views import (
    main,
    serve_register_outlet,
    serve_register_customer,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('hello/', main),
    path('register/outlet/', serve_register_outlet),
    path('register/customer/', serve_register_customer),
    path('refresh/', TokenRefreshView.as_view())
]
