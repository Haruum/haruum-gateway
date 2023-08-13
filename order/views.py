from django.views.decorators.http import require_POST, require_GET
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import order
import json


@require_POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def serve_create_order(request):
    """
    This view serves as the endpoint to create
    an order.
    ---------------------------------------------
    request data must contain:
    customer_email: string
    assigned_outlet_email: string
    pickup_delivery_address: string
    payment_method_id: UUID string
    ordered_items: list

    ordered_items follows the following format
    [
        category_id: UUID string (from outlet service)
        quantity: integer
    ]
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = order.handle_create_order(request.user, request_data)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_get_laundry_orders_of_outlet(request):
    """
    This view returns a list of laundry orders
    assigned to an outlet specified by the email
    parameter.
    ---------------------------------------------
    """
    response_data = order.handle_get_laundry_orders_of_outlet(request.user)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
def serve_get_laundry_progress_statuses(request):
    """
    This view serves as the endpoint to return
    the list of progress status.
    ---------------------------------------------
    """
    response_data = order.handle_get_laundry_progress_statuses()
    return Response(data=response_data)


@require_POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def serve_update_laundry_progress_status(request):
    """
    This method serves as the endpoint to update laundry order
    progress status.
    ---------------------------------------------
    request data must contain:
    laundry_order_id: UUID string
    status_id: UUID string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = order.handle_update_laundry_progress_status(request.user, request_data)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_get_active_laundry_orders_of_a_customer(request):
    """
    This view serves as the endpoint to return the list of
    active orders belonging to a customer.
    ---------------------------------------------
    request param must contain:
    email: string
    """
    response_data = order.handle_get_customer_active_orders(request.user)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_get_completed_laundry_orders_of_a_customer(request):
    """
    This view serves as the endpoint to return the list of
    completed orders belonging to a customer.
    ---------------------------------------------
    """
    response_data = order.handle_get_customer_completed_orders(request.user)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_get_customer_order_details(request):
    """
    This view serves as the endpoint to return the
    details of a laundry order specified by the
    laundry_order_id attribute
    ---------------------------------------------
    request param must contain:
    laundry_order_id: UUID string
    """
    request_data = request.GET
    response_data = order.handle_get_customer_order_details(request.user, request_data)
    return Response(data=response_data)


@require_POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def serve_submit_rating_for_laundry_order(request):
    """
    This view registers a review for a laundry order.
    ---------------------------------------------
    request data must contain:
    laundry_order_id: UUID string
    rating: integer
    comment: string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = order.handle_submit_rating_for_laundry_order(request.user, request_data)
    return Response(data=response_data)

