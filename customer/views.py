from django.views.decorators.http import require_GET, require_POST
from haruum_gateway.decorators import firebase_authenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import customer_management
import json


@require_GET
@api_view(['GET'])
@firebase_authenticated()
def serve_get_customer_data(request):
    """
    This view returns the list of services provided by an outlet.
    """
    response_data = customer_management.handle_get_customer_data(request.user)
    return Response(data=response_data)


@require_POST
@api_view(['POST'])
@firebase_authenticated()
def serve_update_customer_address(request):
    """
    This view updates the customer's latest delivery address,
    along with its coordinates.
    ---------------------------------------------
    request data must contain:
    address: string
    latitude: float
    longitude: float
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = customer_management.handle_update_customer_address(request.user, request_data)
    return Response(data=response_data)
