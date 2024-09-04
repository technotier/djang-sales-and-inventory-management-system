from django.shortcuts import render
from django.views import View

# Create your views here.
class ProfitLossView(View):
    def get(self, request):
        return render(request, "profit_loss.html")