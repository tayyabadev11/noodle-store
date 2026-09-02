from django.shortcuts import render
from .models import Noodle
from .forms import OrderForm
def home(request):
    return render(request, 'noodles/index.html')
def menu(request):
    noodles = Noodle.objects.all()
    return render(request, 'noodles/menu.html', {'noodles': noodles})
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return render(request, 'noodles/order_success.html')
    else:
        form = OrderForm()
    return render(request, 'noodles/order.html', {'form': form})
def about(request):
    return render(request, 'noodles/about.html')
