from haruum_gateway.exceptions import (
    InvalidRequestException,
    FailedToFetchException,
)
from rest_framework import status
import requests


def request_post_and_return_response(request_data, url):
    try:
        response = requests.post(url, json=request_data)
        response_data = response.json()

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise InvalidRequestException(response_data.get('message'))

        if response.status_code >= status.HTTP_500_INTERNAL_SERVER_ERROR:
            raise FailedToFetchException(response_data.get('message'))

        return response_data

    except requests.exceptions.RequestException as exception:
        raise FailedToFetchException('Failed to communicate with external service')