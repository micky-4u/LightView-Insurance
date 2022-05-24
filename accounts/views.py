from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.response import Response
# from knox.models import AuthToken
# from knox.auth import TokenAuthentication
from .serializer import RegisterSerializer, UserSerializer



# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = (TokenAuthentication,)
    
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         user.save()

#         login(request, user)
        
#         return super().post(request, format=None)
    

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({
    #     "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #     "token": AuthToken.objects.create(user)[1]
    #     })
        
        
class UserAPI(generics.RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get_object(self):
        return self.request.user