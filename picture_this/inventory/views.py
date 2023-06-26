# Create your views here.
from django.shortcuts import render, redirect
from .models import Shirt

def add_inventory(request):
    if request.method == 'POST':
        size = request.POST['size']
        color = request.POST['color']
        quantity = int(request.POST['quantity'])

        shirt, created = Shirt.objects.get_or_create(size=size, color=color)
        shirt.quantity += quantity
        shirt.save()

        transaction = Transaction(shirt=shirt, quantity=quantity, action='IN')
        transaction.save()

    return redirect('inventory')

def add_sale(request):
    if request.method == 'POST':
        size = request.POST['size']
        color = request.POST['color']
        quantity = int(request.POST['quantity'])

        shirt = Shirt.objects.get(size=size, color=color)
        shirt.quantity -= quantity
        shirt.save()

        transaction = Transaction(shirt=shirt, quantity=quantity, action='SA')
        transaction.save()

    return redirect('inventory')

def inventory(request):
    shirts = Shirt.objects.all()
    return render(request, 'inventory/inventory.html', {'shirts': shirts})

def history(request):
    transactions = Transaction.objects.all()
    return render(request, 'inventory/history.html', {'transactions': transactions})
