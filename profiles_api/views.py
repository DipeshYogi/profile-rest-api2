from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, filters
from profiles_api import serializers
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
            an_apiview = [
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similar to traditional Django view',
                'Gives you the most cotrol over application logic',
                'Is manually mapped to URL',
            ]


            return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
         """Create a Hello message with our name"""
         serializer = self.serializer_class(data=request.data)
         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             message = f'Hello {name}'
             return Response({'message':message})
         else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request, pk=None):
        """handles partial update"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete objects"""
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer


    def list(self,request):
            a_viewsets = [
                'ViewSets',
            ]

            return Response({'message':'Hello','a_viewset':a_viewsets})



    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)



    def retrieve(self,request,pk=None):
        return Response({'HTTPmethod':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'hhtp_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()

    """adding authentication to only edit own profile"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

    """to search profiles by specific name or any other fields. We will use filters module"""
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')

class UserLoginApiView(ObtainAuthToken):
    """handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
