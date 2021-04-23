from django.urls import path

from .views import ProductDetailView, ProductView

app_name = "products"

urlpatterns = [
    path("", ProductView.as_view(), name="product_list"),
    path("detail/", ProductDetailView.as_view(), name="product_detail"),
]
