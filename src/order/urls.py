from django.urls import path
from . import views

urlpatterns = [
    path("order-list/", views.OrderList.as_view(), name="order_list"),
    path("add-order/", views.AddOrder.as_view(), name="add_order"),
    path("update-order/<int:pk>/", views.UpdateOrder.as_view(), name="update_order"),
    path("delete-order/<int:pk>/", views.DeleteOrder.as_view(), name="delete_order"),
    path("order-detail/<int:pk>/", views.DetailOrder.as_view(), name="order_detail"),
]


