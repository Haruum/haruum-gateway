from rest_framework_simplejwt.tokens import RefreshToken
from ..models import HaruumUser


def get_user_from_email(email):
    return HaruumUser.objects.get(email=email)


def generate_token_for_user(user):
    token: RefreshToken = RefreshToken.for_user(user)
    return {
        'refresh': str(token),
        'access': str(token.access_token)
    }
