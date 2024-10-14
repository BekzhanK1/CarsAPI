from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "account.User", related_name="cars", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.owner}"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        "account.User", related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.car} {self.content} {self.author}"
