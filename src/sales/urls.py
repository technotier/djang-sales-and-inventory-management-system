from django.urls import path
from . import views

urlpatterns = [
    path("sales-list/", views.SalesList.as_view(), name="sales_list"),
    path("add-sales/", views.AddSales.as_view(), name="add_sales"),
    path("update-sales/<int:pk>/", views.UpdateSales.as_view(), name="update_sales"),
    path("delete-sales/<int:pk>/", views.DeleteSales.as_view(), name="delete_sales"),
]
