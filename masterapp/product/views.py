from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from .models import Categoria, Produto


class ProductDetailView(DetailView):
    queryset = Produto.available.all()


class ProductListView(ListView):
    category = None
    paginate_by = 20

    def get_queryset(self):
        queryset = Produto.available.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Categoria, slug=category_slug)
            queryset = queryset.filter(id_categoria=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Categoria.objects.all()
        return context

class ProductBuyList(TemplateView):
    template_name = 'product/produto_buylist.html'

class ProductCheckout(TemplateView):
    template_name = 'product/produto_checkout.html'