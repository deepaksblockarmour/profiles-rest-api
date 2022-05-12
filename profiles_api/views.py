from email import message
from unicodedata import name
from urllib import response
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

    def put(self,request,pk=None):
        """handles updating data"""
        return Response({"method":'PUT'})
    
    def patch(self,request,pk=None):
        """handles partial updating data"""
        return Response({"method":'PATCH'})
    
    def delete(self,request,pk=None):
        """handles deleting data"""
        return Response({"method":'DELETE'})    

class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    """test api viewset"""
    def list(self,request):
        """ Returns a hello message"""
        a_viewset=[
            'uses acrions(list,create,update,partial_update)',
            'automatically maps to urls using Routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'hello!',"a_viewset":a_viewset})
    
    def create(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer._validated_data.get("name")
            message=f"hello{name}!"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrive(self,request,pk=None):
        '''handle getting an object by its ID'''
        return Response({"http_method":"GET"})
        
    def update(self,request,pk=None):
        '''handle updating an object'''
        return Response({"http_method":"PUT"})
        
    def partial_update(self,request,pk=None):
        '''handle updating partially an object by its ID'''
        return Response({"http_method":"PATCH"})
        
    def destroy(self,request,pk=None):
        '''handle removing an object by its ID'''
        return Response({"http_method":"DESTROY "})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)