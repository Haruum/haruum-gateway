from firebase_admin import auth, exceptions as firebase_exceptions
from .exceptions import InvalidCredentialsException
from .utils import get_id_token_from_authorization_header
from main.dto.HaruumUser import HaruumUser


def firebase_authenticated():
    def decorator(view_function_to_decorate):
        def decorated_view_function(*args, **kwargs):
            try:
                request = args[0]
                id_token = get_id_token_from_authorization_header(request.headers.get('Authorization'))
                decoded_token = auth.verify_id_token(id_token)
                request.user = HaruumUser(decoded_token.get('email'))
                return view_function_to_decorate(*args, **kwargs)

            except firebase_exceptions.InvalidArgumentError as exception:
                raise InvalidCredentialsException(str(exception))

        return decorated_view_function

    return decorator





