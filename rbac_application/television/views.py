from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .data import API_DATA

class TelevisionList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        print(request)
        return Response(API_DATA)