from django.views.generic import TemplateView


class ProductView(TemplateView):
    template_name = "product_list.html"


class ProductDetailView(TemplateView):
    template_name = "product_detail.html"
