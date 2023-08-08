from django.db import transaction
from django.views.decorators.http import require_GET, require_POST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .services import auth
import json


@require_GET
@api_view(['GET'])
@permission_classes([])
def main(request):
    response_data = {
        'message': 'Hello, World!'
    }

    return Response(data=response_data)


@require_POST
@api_view(['POST'])
@transaction.atomic()
def serve_register_outlet(request):
    """
    Serves as the endpoint to register an outlet.
    --------------------------------------------
    request data must contain:
    email: string
    phone_number: string
    name: string
    address: string
    latitude: float
    longitude: float
    password: string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = auth.handle_register_outlet(request_data)
    return Response(data=response_data)


@require_POST
@api_view(['POST'])
@transaction.atomic()
def serve_register_customer(request):
    """
    Serves as the endpoint to register a customer.
    --------------------------------------------
    request data must contain:
    email: string
    phone_number: string
    name: string
    address: string
    latitude: float
    longitude: float
    password: string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    response_data = auth.handle_register_customer(request_data)
    return Response(data=response_data)


@require_POST
@api_view(['POST'])
def serve_get_tokens_for_outlet(request):
    """
    Serves as the endpoint for outlets to retrieve
    access and refresh tokens.
    --------------------------------------------
    request data must contain:
    email: string
    password: string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    tokens = auth.handle_login_outlet(request_data)
    return Response(data=tokens)


@require_POST
@api_view(['POST'])
def serve_get_tokens_for_customer(request):
    """
    Serves as the endpoint for customers to retrieve
    access and refresh tokens.
    --------------------------------------------
    email: string
    password: string
    """
    request_data = json.loads(request.body.decode('utf-8'))
    tokens = auth.handle_login_customer(request_data)
    return Response(data=tokens)








