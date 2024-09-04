from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import AddProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Min, Max, Count

# Create your views here.
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class ProductList(View):
    def get(self, request):
        products = Product.objects.all().order_by("-id")
        total_product = Product.objects.all().aggregate(Count("id"))
        sold_out = Product.objects.filter(in_stock = 0).aggregate(Count("id"))
        min_price = Product.objects.aggregate(Min("price"))
        max_price = Product.objects.aggregate(Max("price"))
        #search
        if request.GET.get("search"):
            search = request.GET.get("search")
            products = products.filter(
                Q(name__icontains = search) |
                Q(price__icontains = search) |
                Q(in_stock__icontains = search)
                )
        context = {
            "products": products,
            "total_product": total_product,
            "sold_out": sold_out,
            "min_price": min_price,
            "max_price": max_price
        }
        return render(request, "product_list.html", context)
    
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class AddProduct(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("product_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="user_login"), name="dispatch")
class UpdateProduct(UpdateView):
    model = Product
    form_class = AddProductForm
    template_name = "update_product.html"
    success_url = reverse_lazy("product_list")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
@method_decorator(login_required(login_url="user_login"), name="dispatch")
class DeleteProduct(DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = reverse_lazy("product_list")