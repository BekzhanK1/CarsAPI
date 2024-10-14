from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)


@api_view(["POST"])
def register_view(request):
    email = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")

    if not first_name or not last_name or not password or not email:
        return Response(
            {"error": "Please provide all required fields."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST
        )

    User.objects.create(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=make_password(password),
    )

    return Response(
        {"message": "Successfully registered"}, status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def check_auth_view(request):
    return Response({"message": "You are authenticated"}, status=status.HTTP_200_OK)
