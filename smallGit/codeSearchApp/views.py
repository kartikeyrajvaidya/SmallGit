from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import (LoginRequiredMixin)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json
from rest_framework.response import Response
from django.template.defaultfilters import slugify
from .models import SearchHistory;
from .serializers import SearchHistorySerializer
from rest_framework import generics


class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'codeSearchApp/codeSearchApp_home.html'


class SearchHistoryList(generics.ListCreateAPIView):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_repositories_from_git(request,query):
    query = query.replace(' ','+')
    url = 'https://api.github.com/search/repositories'+'?q='+query
    response = requests.get(url)
    json_data = json.loads(response.text)
    return Response(json_data)



@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_user_from_git(request,query):
    query = query.replace(' ','+')
    url = 'https://api.github.com/search/users'+'?q='+query
    response = requests.get(url)
    json_data = json.loads(response.text)
    return Response(json_data)
