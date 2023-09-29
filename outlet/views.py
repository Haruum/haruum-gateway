from django.views.decorators.http import require_POST, require_GET
from haruum_gateway.decorators import firebase_authenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import outlet
import json


@require_POST
@api_view(['POST'])
@firebase_authenticated()
def serve_update_laundry_outlet_data(request):
    """
    This view updates the laundry outlet data
    (availability status, quota, address)
    ---------------------------------------------
    request data must contain:
    email: (from request user)
    is_available: bool
    quota: integer
    address: string
    phone_number: string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = outlet.handle_update_laundry_outlet_data(request.user, request_data)
    return Response(data=response_data)


@require_POST
@api_view(['POST'])
@firebase_authenticated()
def serve_update_item_laundry_outlet_category_provided(request):
    """
    This view updates the laundry outlet provided services.
    ---------------------------------------------
    request data must contain:
    services_provided: list

    services_provided follows the following format
    {
        service_category_id: uuid string
        price_per_item: float
    }
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = outlet.handle_update_laundry_outlet_category_provided(request.user, request_data)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
def serve_get_reviews_of_outlet(request):
    """
    This view returns the list of reviews for a
    laundry outlet.
    ---------------------------------------------
    request param must contain:
    email: string
    """
    request_data = request.GET
    response_data = outlet.handle_get_reviews_of_outlet(request_data)
    return Response(data=response_data)


@require_GET
@api_view(['GET'])
@firebase_authenticated()
def serve_get_outlet_data(request):
    """
    This view returns the data of the accessing outlet user.
    """
    response_data = outlet.handle_serve_get_outlet_data(request.user)
    return Response(data=response_data)



