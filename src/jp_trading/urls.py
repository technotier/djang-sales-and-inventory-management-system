from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls")),
    path("products/", include("product.urls")),
    path("orders/", include("order.urls")),
    path("accounts/", include("accounts.urls")),
    path("employees/", include("employee.urls")),
    path("sales/", include("sales.urls")),
    path("income/", include("income.urls")),
    path("expense/", include("expense.urls")),
    path("p-and-l-statement/", include("p_n_l.urls")),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
