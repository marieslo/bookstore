from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search


class CatalogView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    allow_empty = True
    slug_url_kwarg = "category_slug"

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        query = self.request.GET.get("q")
        on_sale = self.request.GET.get("on_sale") == "on"
        order_by = self.request.GET.get("order_by")

        if query:
            goods = q_search(query)
            if not goods.exists():
                self.no_results = True
                return Products.objects.all()
            self.no_results = False
        elif category_slug == "all":
            goods = Products.objects.all()
        else:
            goods = Products.objects.filter(category__slug=category_slug)

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Bookstore"
        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
        context["no_results"] = getattr(self, "no_results", False)
        return context




class ProductView(DetailView):

    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context