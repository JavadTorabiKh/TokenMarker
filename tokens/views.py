import requests
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


@api_view(["GET"])
def create_token(request: Request):
    res = requests.get("http://localhost:5000/")
    data = res.json()

    token_serializer = TokenSerializer(data=data["result"])
    if token_serializer.is_valid():
        token_serializer.save()
        return Response({"status": "success", "data": token_serializer.data}, status.HTTP_201_CREATED)
    return Response({"status": "erorrs"}, status.HTTP_400_BAD_REQUEST)


class TokenDetail(generics.RetrieveDestroyAPIView):

    queryset = Token.objects.all()
    serializer_class = TokenSerializer
