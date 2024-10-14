from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cars.models import Car, Comment
from .forms import RegisterForm


# Registration View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("car_list")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


# Car List View
class CarListView(ListView):
    model = Car
    template_name = "car_list.html"
    context_object_name = "cars"


# Car Detail View
class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(car=self.object)
        return context


# Car Create View
class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ["make", "model", "year", "description"]
    template_name = "car_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Car Update View
class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = ["make", "model", "year", "description"]
    template_name = "car_form.html"

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner


# Car Delete View
class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = "car_confirm_delete.html"
    success_url = reverse_lazy("car_list")

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner


# Comment Create View
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    template_name = "comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.car_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.kwargs["pk"]})


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ["make", "model", "year", "description"]
    template_name = "car_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


# Car Update View
class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = ["make", "model", "year", "description"]
    template_name = "car_form.html"

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})
