import os

import jwt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

from user.models import User


class JWTAuthenticationMiddleware(BaseAuthentication):

    def authenticate(self, request):

        jwt_token = request.headers.get('Authorization', None)
        if not jwt_token:
            return None

        try:
            jwt_options = {
                'verify_signature': True,
                'verify_exp': True,
                'verify_nbf': False,
                'verify_iat': True,
                'verify_aud': False
            }
            payload = jwt.decode(jwt_token, settings.SECRET_KEY,
                                 algorithms=['HS256', ], options=jwt_options)
            user_id = payload['user_id']
            user = User.objects.get(id=user_id)

            return user, jwt_token
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Token is invalid')
        except User.DoesNotExist:
            raise AuthenticationFailed
