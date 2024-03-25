import jwt
from django.conf import settings

jwt_token = jwt.encode({'user_id': "1"}, "django-insecure-5@t!^6mw4#74=u#p@$*3ph716=#3tsml^bws*ts6h$n)&rd__l",
                       algorithm="HS256")
print(jwt_token)
