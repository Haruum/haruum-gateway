from haruum_gateway import utils as haruum_gateway_utils
from haruum_gateway.settings import (
    CUSTOMER_DETAILS_URL,
    CUSTOMER_UPDATE_ADDRESS_URL,
)


def handle_get_customer_data(user):
    request_data = {'email': user.get_email()}
    response_data = haruum_gateway_utils.request_get_and_return_response(request_data, CUSTOMER_DETAILS_URL)
    return response_data


def transform_customer_address_update(customer_email, request_data):
    request_data['email'] = customer_email
    return request_data


def handle_update_customer_address(user, request_data: dict):
    transformed_request_data = transform_customer_address_update(user.get_email(), request_data)
    response_data = haruum_gateway_utils.request_post_and_return_response(
        transformed_request_data,
        CUSTOMER_UPDATE_ADDRESS_URL
    )
    return response_data
