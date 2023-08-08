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


def register_user_in_auth(request_data):
    try:
        email = request_data.get('email')
        HaruumUser.objects.create_user(email=email)

    except IntegrityError:
        raise InvalidRequestException(f'User with email {request_data.get("email")} already exists')


def handle_register_outlet(request_data):
    register_user_in_auth(request_data)
    response_data = haruum_gateway_utils.request_post_and_return_response(request_data, OUTLET_REGISTRATION_URL)
    return response_data


def handle_register_customer(request_data):
    register_user_in_auth(request_data)
    response_data = haruum_gateway_utils.request_post_and_return_response(request_data, CUSTOMER_REGISTRATION_URL)
    return response_data


def validate_email_and_password_of_user(request_data, validation_url):
    response_data = haruum_gateway_utils.request_post_and_return_response(request_data, validation_url)

    if not response_data.get('password_is_for_email'):
        raise InvalidCredentialsException('Invalid email or password provided')


def handle_login_outlet(request_data):
    validate_email_and_password_of_user(request_data, OUTLET_CREDENTIALS_URL)
    user = utils.get_user_from_email(request_data.get('email'))
    return utils.generate_token_for_user(user)


def handle_login_customer(request_data):
    validate_email_and_password_of_user(request_data, CUSTOMER_CREDENTIALS_URL)
    user = utils.get_user_from_email(request_data.get('email'))
    return utils.generate_token_for_user(user)

