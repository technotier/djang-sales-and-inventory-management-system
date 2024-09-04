from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy
from django.db.models import Sum
from django.utils.timezone import datetime
from datetime import date, timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator

today = datetime.today()
yesterday = today - timedelta(days=1)
this_month = timezone.now().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
last_month = date.today().replace(day=1) - timedelta(days=1)

# Create your views here.
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class Expense_list(View):
    def get(self, request):
        expenses = Expense.objects.all().order_by("-id")
        today_expense = Expense.objects.filter(date = today).aggregate(Sum("expense_amount"))
        yesterday_expense = Expense.objects.filter(date = yesterday).aggregate(Sum("expense_amount"))
        this_month_expense = Expense.objects.filter(date__gte = this_month).aggregate(Sum("expense_amount"))
        last_month_expense = Expense.objects.filter(date__lte = last_month).aggregate(Sum("expense_amount"))
        #search
        if request.GET.get("search"):
            search = request.GET.get("search")
            expenses = expenses.filter(
                Q(expense_type__icontains = search) |
                Q(paid_to__icontains = search) |
                Q(expense_amount__icontains = search) |
                Q(payment_type__icontains = search)
                )
        paginator = Paginator(expenses, 30)
        page_number = request.GET.get("page")
        expenses = paginator.get_page(page_number)
        context = {
            "expenses": expenses,
            "today_expense": today_expense,
            "yesterday_expense": yesterday_expense,
            "this_month_expense": this_month_expense,
            "last_month_expense": last_month_expense
        }
        return render(request, "expense_list.html", context)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class AddExpense(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "add_expense.html"
    success_url = reverse_lazy("expense_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class UpdateExpense(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "update_expense.html"
    success_url = reverse_lazy("expense_list")

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DeleteExpense(DeleteView):
    model = Expense
    template_name = "delete_expense.html"
    success_url = reverse_lazy("expense_list")
    
