from django.http import HttpResponse
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("", lambda x: HttpResponse("Hello World"), name="accounts"),
]
