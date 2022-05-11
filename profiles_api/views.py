from unicodedata import name
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import seriallizers

class HelloApiView(APIView):
    '''test api view'''
    serializer_class=serializers.HelloSerializer


    def get(self,request,format=None):
        """returns a list of api view"""
        an_apiview=[
            "uses http methods as function(get,post,patch,put,delete) ",
            "is similar to a traditional django view",
            "gives you the most control over your application logic",
            "is mapped manually to urls"
        ]
        return Response({'key':'hello','an_apiview':an_apiview})

    def post(self,request):
        """create  a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )