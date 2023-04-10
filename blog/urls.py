from django.urls import path
from .views import home_page, single_post

urlpatterns = [
    path("", home_page, name="home_page"),
    path("post/<int:pk>", single_post, name="single_post"),
]
