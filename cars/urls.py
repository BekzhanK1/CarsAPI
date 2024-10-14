from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from cars.views import CarViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"cars", CarViewSet, basename="cars")

cars_router = NestedDefaultRouter(router, r"cars", lookup="car")
cars_router.register(r"comments", CommentViewSet, basename="car-comments")

urlpatterns = router.urls + cars_router.urls
