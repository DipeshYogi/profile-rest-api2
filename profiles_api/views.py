from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
            an_apiview = [
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similar to traditional Django view',
                'Gives you the most cotrol over application logic',
                'Is manually mapped to URL',
            ]


            return Response({'message':'Hello','an_apiview':an_apiview})
