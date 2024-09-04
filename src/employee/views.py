from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Count

# Create your views here.
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class AddEmployee(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "add_employee.html"
    success_url = reverse_lazy("employee_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class EmployeeList(ListView):
    model = Employee
    template_name = "employee_list.html"
    context_object_name = "employee"
    ordering = ["-id"]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_employee"] = Employee.objects.aggregate(Count("id"))
        context["total_department"] = Employee.objects.aggregate(Count("department"))
        context["total_salary"] = Employee.objects.aggregate(Sum("salary"))
        return context

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class UpdateEmployee(UpdateView):
    model = Employee
    form_class  = EmployeeForm
    template_name = "update_employee.html"
    success_url = reverse_lazy("employee_list")

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DeleteEmployee(DeleteView):
    model = Employee
    template_name = "delete_employee.html"
    success_url = reverse_lazy("employee_list")