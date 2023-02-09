from django.http import HttpResponse
from .models import ShoppingListItem
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'shopping_list/index.html')


def add(request):
    return HttpResponse("Add page")


def view(request):
    shoppingList = ShoppingListItem.objects.order_by("id")
    context = {'shoppingList': shoppingList}
    return render(request, 'shopping_list/view.html', context)


def detail(request, itemId):
    item = get_object_or_404(ShoppingListItem, pk=itemId)
    context = {'item': item}
    return render(request, 'shopping_list/detail.html', context)
