from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page - Car List
    path("", views.CarListView.as_view(), name="car_list"),
    # Car Detail
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    # Add Car
    path("add-car/", views.CarCreateView.as_view(), name="add_car"),
    # Edit Car
    path("cars/<int:pk>/edit/", views.CarUpdateView.as_view(), name="edit_car"),
    # Delete Car
    path("cars/<int:pk>/delete/", views.CarDeleteView.as_view(), name="delete_car"),
    # Add Comment
    path(
        "cars/<int:pk>/comments/", views.CommentCreateView.as_view(), name="add_comment"
    ),
    # Login page
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    # Logout page
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    # Register page
    path("register/", views.register_view, name="register"),
]
