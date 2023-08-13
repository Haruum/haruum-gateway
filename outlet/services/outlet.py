from haruum_gateway import utils as haruum_gateway_utils
from haruum_gateway.settings import (
    OUTLET_UPDATE_URL,
    OUTLET_UPDATE_SERVICE_URL,
    ORDER_GET_OUTLET_REVIEWS_URL,
)


def transform_laundry_outlet_update_data(outlet_email, request_data):
    request_data['email'] = outlet_email
    return request_data


def handle_update_laundry_outlet_data(user, request_data: dict):
    transformed_request_data = transform_laundry_outlet_update_data(user.get_email(), request_data)
    response_data = haruum_gateway_utils.request_post_and_return_response(transformed_request_data, OUTLET_UPDATE_URL)
    return response_data


def handle_update_laundry_outlet_category_provided(user, request_data: dict):
    transformed_request_data = transform_laundry_outlet_update_data(user.get_email(), request_data)
    response_data = haruum_gateway_utils.request_post_and_return_response(
        transformed_request_data,
        OUTLET_UPDATE_SERVICE_URL
    )
    return response_data


def handle_get_reviews_of_outlet(request_data):
    response_data = haruum_gateway_utils.request_get_and_return_response(request_data, ORDER_GET_OUTLET_REVIEWS_URL)
    return response_data

