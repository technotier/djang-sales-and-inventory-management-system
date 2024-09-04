from django.urls import path
from . import views

urlpatterns = [
    path("product-list/", views.ProductList.as_view(), name="product_list"),
    path("add-product/", views.AddProduct.as_view(), name="add_product"),
    path("update-product/<int:pk>/", views.UpdateProduct.as_view(), name="update_product"),
    path("delete-product/<int:pk>/", views.DeleteProduct.as_view(), name="delete_product"),
]
