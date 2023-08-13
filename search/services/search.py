from haruum_gateway import utils as haruum_gateway_utils
from haruum_gateway.settings import (
    OUTLET_ALL_OUTLETS_URL,
    OUTLET_DETAIL_URL,
    OUTLET_SERVICES_URL,
)


def handle_get_outlet(request_data):
    response_data = haruum_gateway_utils.request_get_and_return_response(request_data, OUTLET_ALL_OUTLETS_URL)
    return response_data


def handle_get_outlet_details(request_data):
    response_data = haruum_gateway_utils.request_get_and_return_response(request_data, OUTLET_DETAIL_URL)
    return response_data


def handle_get_outlet_services(request_data):
    response_data = haruum_gateway_utils.request_get_and_return_response(request_data, OUTLET_SERVICES_URL)
    return response_data


