from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, viewsets

from user.models import User, Page
from user.serializers import UserSerializer, PageSerializer
from user.services import register_user_service, authenticate_user_service, logout_service, get_tags, create_page_with_tags
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


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        create_page_with_tags(serializer, request)
        return Response({"status": "200"})


class AllUsersViewSet(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
