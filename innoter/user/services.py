from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from user.models import User, Tag
from user.utils import generate_access_token
from django.db import IntegrityError


# USER REGISTRATION SERVICE
def register_user_service(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    try:
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

    except IntegrityError as error:
        if 'unique constraint' in str(error).lower() and 'email' in str(error).lower():
            response_text = "This email is already used"
        else:
            response_text = "User already exists"
        return Response({"error": response_text}, status=status.HTTP_400_BAD_REQUEST)

    token = generate_access_token(user)
    return Response({"token": token})


def authenticate_user_service(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    token = generate_access_token(user)

    if user:
        return Response({"token": token})
    else:
        return Response({'error': 'User is not credentials'})


def logout_service():
    response = Response({'success': 'Successfully logged out'})
    response.delete_cookie('jwt')
    return response


def get_tags(request) -> list:
    tags = []
    tag_names = request.data.pop('tags')
    # print(tag_names, 'tag_names')
    if tag_names:
        # tag_names = request.data.get('tags')
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name['name'])
            # print(created)
            tags.append(tag.id)
    return tags


def create_page_with_tags(serializer, request):
    tags = get_tags(request)
    page = create_page(serializer)

    if tags:
        add_tags_to_page(tags, page)

    return page


def create_page(serializer):
    serializer.is_valid(raise_exception=True)
    # print(serializer.errors)
    return serializer.save()


def add_tags_to_page(tags, page):
    page.tags.set(tags)
