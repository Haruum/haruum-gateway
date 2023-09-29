from django.db.utils import IntegrityError
from haruum_gateway import utils as haruum_gateway_utils
from haruum_gateway.exceptions import (
    InvalidCredentialsException,
    InvalidRequestException
)
from haruum_gateway.settings import (
    OUTLET_REGISTRATION_URL,
    OUTLET_CREDENTIALS_URL,
    CUSTOMER_REGISTRATION_URL,
    CUSTOMER_CREDENTIALS_URL,
)
from ..models import HaruumUser
from . import utils


def handle_register_outlet(request_data):
    response_data = haruum_gateway_utils.request_post_and_return_response(request_data, OUTLET_REGISTRATION_URL)
    return response_data


def handle_register_customer(request_data):
    response_data = haruum_gateway_utils.request_post_and_return_response(request_data, CUSTOMER_REGISTRATION_URL)
    return response_data



