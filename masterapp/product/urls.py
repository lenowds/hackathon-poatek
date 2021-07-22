from django.urls import path, include
from .views import ProductDetailView, ProductListView, ProductBuyList, ProductCheckout

app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("buylist/", ProductBuyList.as_view(), name="buylist"),
    path("checkout/", ProductCheckout.as_view(), name="checkout"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("des_categoria/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
    
]