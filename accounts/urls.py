# from knox import views as knox_views
# from .views import LoginAPI
from django.urls import path, include
from .views import RegisterAPI, login_api
from knox import views as knox_views


urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path('login/', login_api),
    path(r'logout/', knox_views.LogoutView.as_view(), name='logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
