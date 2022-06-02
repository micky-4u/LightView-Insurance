from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializer import RegisterSerializer, UserSerializer
from rest_framework.decorators import api_view 
from rest_framework.views import APIView


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token = AuthToken.objects.create(user)[1]
    
    return Response({
        "user_info": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        },
        "token":token
    })
    

# Register API
class RegisterAPI(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        
        return Response({
        "user_info": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
        "token":token
    })    

        
        
class UserAPI(generics.RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    