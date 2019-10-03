from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
