from django.shortcuts import render, redirect
from .models import Item
from . import forms

def items_list(request):
    items = Item.objects.all()
    return render(request, 'items/items_list.html', {'items': items})

def item_page(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'items/item_page.html', { 'item': item})

def item_new(request):
    if request.method == "POST":
        form = forms.CreateItem(request.POST, request.FILES)
        if form.is_valid():
            newitem = form.save(commit=False)
            newitem.save()
            return redirect('items:list')
    else:
        form = forms.CreateItem()
    return render(request, 'items/item_new.html', {'form':form})