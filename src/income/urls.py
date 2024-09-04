from django.urls import path
from . import views

urlpatterns = [
    path("income-list/", views.IncomeList.as_view(), name="income_list"),
    path("add-income/", views.AddIncome.as_view(), name="add_income"),
    path("update-income/<int:pk>/", views.UpdateIncome.as_view(), name="update_income"),
    path("delete-income/<int:pk>/", views.DeleteIncome.as_view(), name="delete_income"),
]

