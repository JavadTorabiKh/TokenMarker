from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Token, User
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import TokenSerializer, UserSerializer


@api_view(["GET", "PUT", "DELETE"])
def get_users(request: Request):

    try:
        user = User.objects.all()
        print(user)
    except User.DoesNotExist:
        return Response({"status": "erorr"}, status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        todo_serializer = UserSerializer(user, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
