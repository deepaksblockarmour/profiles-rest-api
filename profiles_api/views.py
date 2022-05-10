from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    '''test api view'''
    
    def get(sellf,request,format=None):
        """returns a list of api view"""
        an_apiview=[
            "uses http methods as function(get,post,patch,put,delete) ",
            "is similar to a traditional django view",
            "gives you the most control over your application logic",
            "is mapped manually to urls"
        ]
        return Response({'key':'hello','an_apiview':an_apiview})