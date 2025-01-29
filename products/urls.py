
from django.urls import path
from .views import *

app_name = "products"

urlpatterns = [

    path("", ProductListView.as_view(), name="product_list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("category/<slug:slug>/", CategoryListView.as_view(), name="category_list"),
    path("brand/<str:name>/", BrandListView.as_view(), name="brand_list"),


]
