from rest_framework.views import exception_handler
from rest_framework.response import Response
from .exceptions import (
    RestrictedAccessException,
    FailedToFetchException,
    InvalidRequestException,
    InvalidCredentialsException
)


def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)
    if response is not None:
        return response

    if isinstance(exception, InvalidRequestException):
        status_code = 400

    elif isinstance(exception, InvalidCredentialsException):
        status_code = 401

    elif isinstance(exception, RestrictedAccessException):
        status_code = 403

    elif isinstance(exception, FailedToFetchException):
        status_code = 502

    else:
        status_code = 500

    return Response({'message': str(exception)}, status=status_code)

