from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .models import Car, Comment
from .serializers import CarSerializer, CommentSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data["owner"] = request.user.id
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise PermissionDenied("You can't update this car.")
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise PermissionDenied("You can't delete this car.")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CommentSerializer

    def get_queryset(self):
        car_id = self.kwargs["car_pk"]
        return Comment.objects.filter(car=car_id)

    def create(self, request, *args, **kwargs):
        data = request.data
        data["author"] = request.user.id
        data["car"] = self.kwargs["car_pk"]
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied("You can't update this comment.")
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied("You can't delete this comment.")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
