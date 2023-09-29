from haruum_gateway import utils as haruum_gateway_utils
from haruum_gateway.exceptions import RestrictedAccessException
from haruum_gateway.settings import (
    ORDER_CREATION_URL,
    ORDER_GET_ORDERS_OF_OUTLET_URL,
    ORDER_ALL_STATUS,
    ORDER_DETAILS_URL,
    ORDER_UPDATE_STATUS_URL,
    ORDER_CUSTOMER_ACTIVE_URL,
    ORDER_CUSTOMER_COMPLETED_URL,
    ORDER_SUBMIT_REVIEW_URL,
)


def transform_create_order_request(customer_email, request_data):
    request_data['customer_email'] = customer_email
    return request_data


def handle_create_order(user, request_data: dict):
    transformed_request_data = transform_create_order_request(user.get_email(), request_data)
    response_data = haruum_gateway_utils.request_post_and_return_response(transformed_request_data, ORDER_CREATION_URL)
    return response_data


def add_email_to_request_data(email, request_data):
    request_data['email'] = email
    return request_data


def handle_get_laundry_orders_of_outlet(user):
    transformed_request_data = add_email_to_request_data(user.get_email(), {})
    response_data = haruum_gateway_utils.request_get_and_return_response(
        transformed_request_data,
        ORDER_GET_ORDERS_OF_OUTLET_URL
    )
    return response_data


def handle_get_laundry_progress_statuses():
    response_data = haruum_gateway_utils.request_get_and_return_response({}, ORDER_ALL_STATUS)
    return response_data


def get_laundry_order_details(laundry_order_id):
    order_details_request_data = {'laundry_order_id': laundry_order_id}
    order_data = haruum_gateway_utils.request_get_and_return_response(order_details_request_data, ORDER_DETAILS_URL)
    return order_data


def validate_outlet_laundry_order_ownership(user, laundry_order_data):
    if laundry_order_data.get('assigned_outlet_email') != user.get_email():
        raise RestrictedAccessException(f'Outlet {user.get_email()} is not the assigned outlet of order')


def handle_update_laundry_progress_status(user, request_data):
    laundry_order_details = get_laundry_order_details(request_data.get('laundry_order_id'))
    validate_outlet_laundry_order_ownership(user, laundry_order_details)
    update_response_data = haruum_gateway_utils.request_post_and_return_response(request_data, ORDER_UPDATE_STATUS_URL)
    return update_response_data


def handle_get_customer_active_orders(user):
    transformed_request_data = add_email_to_request_data(user.get_email(), {})
    customer_orders_response_data = haruum_gateway_utils.request_get_and_return_response(
        transformed_request_data,
        ORDER_CUSTOMER_ACTIVE_URL
    )
    return customer_orders_response_data


def handle_get_customer_completed_orders(user):
    transformed_request_data = add_email_to_request_data(user.get_email(), {})
    customer_orders_response_data = haruum_gateway_utils.request_get_and_return_response(
        transformed_request_data,
        ORDER_CUSTOMER_COMPLETED_URL
    )
    return customer_orders_response_data


def validate_customer_laundry_order_ownership(user, laundry_order_data):
    if laundry_order_data.get('owning_customer_email') != user.get_email():
        raise RestrictedAccessException(f'Customer {user.get_email()} is not the owner of order')


def handle_get_customer_order_details(user, request_data):
    laundry_order_details = get_laundry_order_details(request_data.get('laundry_order_id'))
    validate_customer_laundry_order_ownership(user, laundry_order_details)
    return laundry_order_details


def handle_get_outlet_order_details(user, request_data):
    laundry_order_details = get_laundry_order_details(request_data.get('laundry_order_id'))
    validate_outlet_laundry_order_ownership(user, laundry_order_details)
    return laundry_order_details


def handle_submit_rating_for_laundry_order(user, request_data):
    laundry_order_details = get_laundry_order_details(request_data.get('laundry_order_id'))
    validate_customer_laundry_order_ownership(user, laundry_order_details)
    response_data = haruum_gateway_utils.request_post_and_return_response(request_data, ORDER_SUBMIT_REVIEW_URL)
    return response_data

