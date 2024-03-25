from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer
from user.services import register_user_service, authenticate_user_service, logout_service
from user.utils import generate_access_token


class RegistrationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        return register_user_service(request)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return authenticate_user_service(request)

        # user = User.objects.get(username=request.data['username'], password=request.data['password'])
        # print(user, 'user')
        # jwt_token = generate_access_token(user)
        # print(jwt_token, 'token')
        # return Response({"status": "ok"})


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return logout_service()


class start(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse({"start page": 'ok'})
