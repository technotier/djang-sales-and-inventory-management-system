from django.urls import path
from . import views

urlpatterns = [
    # path("expense-list/", views.expense_list, name="expense_list"),
    path("expense-list/", views.Expense_list.as_view(), name="expense_list"),
    path("add-expense/", views.AddExpense.as_view(), name="add_expense"),
    path("update-expense/<int:pk>/", views.UpdateExpense.as_view(), name="update_expense"),
    path("delete-expense/<int:pk>/", views.DeleteExpense.as_view(), name="delete_expense"),
]

