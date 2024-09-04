from django.shortcuts import render
from .models import Sales
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils.timezone import datetime
from django.db.models import Sum, Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import SalesForm

# some date time calculation
today = datetime.today()

# Create your views here.
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class SalesList(View):
    def get(self, request):
        sales = Sales.objects.all().order_by("-id")
        today_sales = Sales.objects.filter(date = today).aggregate(Count("id"))
        total_amount = Sales.objects.filter(date = today).aggregate(Sum("invoice_total"))
        received_amount = Sales.objects.filter(date = today).aggregate(Sum("payment_receive"))
        due_amount = Sales.objects.filter(date = today).aggregate(Sum("due_payment"))
        #search
        if request.GET.get("search"):
            search = request.GET.get("search")
            sales = sales.filter(
                Q(customer__icontains = search) |
                Q(phone__icontains = search) |
                Q(invoice_number__icontains = search) |
                Q(payment_status__icontains = search)
                )
        paginator = Paginator(sales, 50)
        page_number = request.GET.get("page")
        sales = paginator.get_page(page_number)
        context = {
            "sales": sales,
            "today_sales": today_sales,
            "total_amount": total_amount,
            "received_amount": received_amount,
            "due_amount": due_amount
        }
        return render(request, "sales_list.html", context)
    
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class AddSales(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = "add_sales.html"
    success_url = reverse_lazy("sales_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class UpdateSales(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = "update_sales.html"
    success_url = reverse_lazy("sales_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DeleteSales(DeleteView):
    model = Sales
    template_name = "delete_sales.html"
    success_url = reverse_lazy("sales_list")
