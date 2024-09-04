from django.urls import path
from . import views

urlpatterns = [
    path("add-employee/", views.AddEmployee.as_view(), name="add_employee"),
    path("employee-list/", views.EmployeeList.as_view(), name="employee_list"),
    path("update-employee/<int:pk>/", views.UpdateEmployee.as_view(), name="update_employee"),
    path("delete-employee/<int:pk>/", views.DeleteEmployee.as_view(), name="delete_employee"),
]

