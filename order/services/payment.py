from haruum_gateway import utils as haruum_gateway_utils
from haruum_gateway.settings import ORDER_PAYMENT_METHODS_URL


def handle_get_payment_methods():
    response_data = haruum_gateway_utils.request_get_and_return_response({}, ORDER_PAYMENT_METHODS_URL)
    return response_data
