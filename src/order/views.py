from django.shortcuts import render
from django.views import View
from .models import Order
from .forms import OrderForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Count
from django.utils.timezone import datetime
from datetime import date, timedelta
from django.utils import timezone

# some date and time calculation
today = datetime.today()
this_month = timezone.now().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
last_month = date.today().replace(day=1) - timedelta(days=1)

# Create your views here.
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class OrderList(View):
    def get(self, request):
        orders = Order.objects.all().order_by("-id")
        
        today_order = Order.objects.filter(date = today).aggregate(Count("id"))
        total_amount = Order.objects.filter(date = today).aggregate(Sum("total_amount"))
        this_month_order = Order.objects.filter(date__gte = this_month).aggregate(Sum("total_amount"))
        last_month_order = Order.objects.filter(date__lte = last_month).aggregate(Sum("total_amount"))
        #search
        if request.GET.get("search"):
            search = request.GET.get("search")
            orders = orders.filter(
                Q(customer__icontains = search) |
                Q(phone__icontains = search) |
                Q(id__icontains = search) |
                Q(total_amount__icontains = search)
                )
        paginator = Paginator(orders, 50)
        page_number = request.GET.get("page")
        orders = paginator.get_page(page_number)
        context = {
            "orders": orders,
            "today_order": today_order,
            "total_amount": total_amount,
            "this_month_order": this_month_order,
            "last_month_order": last_month_order
        }
        return render(request, "order_list.html", context)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class AddOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "add_order.html"
    success_url = reverse_lazy("order_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class UpdateOrder(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "update_order.html"
    success_url = reverse_lazy("order_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DeleteOrder(DeleteView):
    model = Order
    template_name = "delete_order.html"
    success_url = reverse_lazy("order_list")

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DetailOrder(DetailView):
    model = Order
    template_name = "order_detail.html"