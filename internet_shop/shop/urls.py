from django.urls import path
from . import views

urlpatterns = [

    path("", views.ProductListView.as_view(), name="product_list"),
    path("add_basket/", views.AddBasket.as_view(), name="add_basket"),
    path("product_detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("basket/", views.BasketListView.as_view(), name="basket"),
    path("category_list/<slug:slug>/", views.CategoryList.as_view(), name="category_list"),
    path("search_product/", views.ProductSearch.as_view(), name="search_product"),
    path("/", views.BasketDeleteAll, name="delete_all_from_basket"),
    path("basket/<int:pk>", views.BasketDeleteOne.as_view(), name="delete_one"),
]
