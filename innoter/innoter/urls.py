from django.contrib import admin
from django.urls import path, include

from user.views import RegistrationAPIView, LoginAPIView, start, LogoutAPIView

urlpatterns = [
    path('user/', include('user.urls', namespace='user')),
    path('admin/', admin.site.urls),
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('', start.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]
