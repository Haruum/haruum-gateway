from haruum_gateway.exceptions import (
    InvalidRequestException,
    FailedToFetchException,
    InvalidCredentialsException
)
from rest_framework import status
import requests


def request_post_and_return_response(request_data, url):
    try:
        response = requests.post(url, json=request_data)
        response_data = response.json()

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise InvalidRequestException(response_data.get('message'))

        if response.status_code != status.HTTP_200_OK:
            raise FailedToFetchException(response_data.get('message'))

        return response_data

    except requests.exceptions.RequestException:
        raise FailedToFetchException('Failed to communicate with external service')


def request_get_and_return_response(request_data, url):
    try:
        modified_url = query_builder(url, request_data)

        response = requests.get(modified_url)
        response_data = response.json()

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise InvalidRequestException(response_data.get('message'))

        if response.status_code != status.HTTP_200_OK:
            raise FailedToFetchException(f'{response.status_code}: {response_data.get("message")}')

        return response_data

    except requests.exceptions.RequestException :
        raise FailedToFetchException('Failed to communicate with external service')


def query_builder(base_url, params):
    modified_url = base_url + '?'

    for k, v in params.items():
        modified_url = f'{modified_url}{k}={v}&'

    return modified_url[:-1]


def get_id_token_from_authorization_header(authorization_header):
    try:
        return authorization_header.split()[1]

    except AttributeError:
        raise InvalidCredentialsException('No token was provided')

    except IndexError:
        raise InvalidCredentialsException('Given token is invalid')


