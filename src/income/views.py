from django.shortcuts import render
from .models import Income
from .forms import IncomeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

# Create your views here.
today = datetime.today()
yesterday = today - timedelta(days=1)
this_month = timezone.now().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
last_month = date.today().replace(day=1) - timedelta(days=1)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class IncomeList(View):
    def get(self, request):
        income = Income.objects.all().order_by("-id")
        today_income = Income.objects.filter(date = today).aggregate(Sum("amount"))
        yesterday_income = Income.objects.filter(date = yesterday).aggregate(Sum("amount"))
        this_month_income = Income.objects.filter(date__gte = this_month).aggregate(Sum("amount"))
        last_month_income = Income.objects.filter(date__lte = last_month).aggregate(Sum("amount"))
        #search
        if request.GET.get("search"):
            search = request.GET.get("search")
            income = income.filter(
                Q(income_type__icontains = search) |
                Q(total_invoice__icontains = search) |
                Q(amount__icontains = search)
                )
        paginator = Paginator(income, 30)
        page_number = request.GET.get("page")
        income = paginator.get_page(page_number)
        context = {
            "income": income,
            "today_income": today_income,
            "yesterday_income": yesterday_income,
            "this_month_income": this_month_income,
            "last_month_income": last_month_income
        }
        return render(request, "income_list.html", context)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class AddIncome(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = "add_income.html"
    success_url = reverse_lazy("income_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class UpdateIncome(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "update_income.html"
    success_url = reverse_lazy("income_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DeleteIncome(DeleteView):
    model = Income
    template_name = "delete_income.html"
    success_url = reverse_lazy("income_list")