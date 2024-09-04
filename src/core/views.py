from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from order.models import Order
from sales.models import Sales
from product.models import Product
from django.db.models import Sum, Count
from django.utils import timezone
from django.utils.timezone import datetime

# some data time calculation
today = datetime.today()
this_month = timezone.now().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )

# Create your views here.
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class IndexViwew(View):
    def get(self, request):
        total_orders = Order.objects.aggregate(Count("id"))
        total_order_amount = Order.objects.aggregate(Sum("total_amount"))
        total_sales = Sales.objects.aggregate(Count("id"))
        total_sales_amount = Sales.objects.aggregate(Sum("invoice_total"))
        
        last_10_sales = Sales.objects.all().filter(date = today ).order_by("-id")[:10]
        top_5_sales = Sales.objects.filter(date__gte = this_month).order_by("-invoice_total")[:5]
        
        products = Order.objects.annotate(qty = Sum("line_one_qty")).order_by("-line_one_qty")
        
        payment_receive_total = Sales.objects.aggregate(Sum("payment_receive"))
        due_payment_total = Sales.objects.aggregate(Sum("due_payment"))
        context = {
            "total_orders": total_orders,
            "total_order_amount": total_order_amount,
            "total_sales": total_sales,
            "total_sales_amount": total_sales_amount,
            "last_10_sales": last_10_sales,
            "top_5_sales": top_5_sales,
            "payment_receive_total": payment_receive_total,
            "due_payment_total": due_payment_total,
            "products": products
        }
        return render(request, "index.html", context)

