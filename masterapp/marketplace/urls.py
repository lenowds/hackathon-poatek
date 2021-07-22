from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import MarketplaceCreate

app_name = "marketplace"

urlpatterns = [
    path("", MarketplaceCreate.as_view(), name='create'),
]