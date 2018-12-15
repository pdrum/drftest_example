from drftest.auth_provider import AuthProvider
from rest_framework.authtoken.models import Token


class TokenAuthProvider(AuthProvider):
    def set_auth(self, api_client, user):
        if user is None:
            return
        token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def get_auth_headers(self, user):
        if user is None:
            return {}
        token, _ = Token.objects.get_or_create(user=user)
        return {'AUTHORIZATION': 'Token ' + token.key}
