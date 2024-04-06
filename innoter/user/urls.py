from django.contrib import admin
from django.urls import path

from user.views import PageViewSet, AllUsersViewSet

app_name = 'user'
urlpatterns = [
    path('page/', PageViewSet.as_view({'post': 'create'})),
    path('all_users/', AllUsersViewSet.as_view())
]
