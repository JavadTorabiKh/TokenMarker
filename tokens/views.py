from rest_framework import status
from .models import Token, User
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import TokenSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


class PaginationSize(PageNumberPagination):
    page_size = 3


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PaginationSize

    # authentication
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TokenList(generics.ListCreateAPIView):

    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    pagination_class = PaginationSize

    # authentication
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class TokenDetail(generics.RetrieveDestroyAPIView):

    queryset = Token.objects.all()
    serializer_class = TokenSerializer
