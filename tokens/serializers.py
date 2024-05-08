from rest_framework import serializers
from .models import User, Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'pblicKey']


# class TokenSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Token
#         fields = ['id', 'user', 'address', 'token_type', 'count']


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Token
        fields = ['id', 'user', 'address', 'token_type', 'count']

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        token = Token.objects.create(user=user, **validated_data)
        return token
