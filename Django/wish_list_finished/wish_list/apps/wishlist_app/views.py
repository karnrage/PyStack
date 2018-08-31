from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..loginregis_app.models import User, UserManager, Item
from django.contrib import messages
from datetime import date
from django.urls import reverse

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    current_user = User.objects.get(id=request.session['user_id'])
    all_wishlist = Item.objects.exclude(id=request.session['user_id'])
    all_list = Item.objects.all()
    my_wishlist = current_user.listed_items.all()
    Users = User.objects.all()

    #Display everyone but user's items --------------------
    Other_listing = Item.objects.exclude(listed_by=current_user)
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'my_wishlist': my_wishlist,
        'Users': Users,
        'all_wishlist': all_wishlist,
        'Other_listing': Other_listing,
 
    }

    return render(request, 'wishlist/index.html', context)


def addingitem_page(request):
# -- Make an item PAGE -----

    return render(request, 'wishlist/add.html')

def submit_item(request):
# -- MAKING/ADDING item -----
    result = User.objects.item_validator(request.POST)
    print result
    if type(result) == list:
        if len(result) > 0:
            messages.error(request, result)
        return redirect(reverse('wishlist:addingitem_page'))

    if request.method == "POST":
        current_user = User.objects.get(id=request.session['user_id'])
        this_item = Item.objects.create(product=request.POST['product'], uploader=current_user)
        this_item.listed_by.add(current_user)
        current_user.listed_items.add(this_item)
        this_item.save()
        current_user.save()
        print request.POST

    return redirect(reverse('wishlist:index'))

def show(request, Item_id):
#To display an item -----------------------------------------
    Current_item = Item.objects.get(id=Item_id)
    this_item = Current_item.listed_by.all()
    context = {
        'Item': Item.objects.get(id=Item_id),
        'this_item': this_item
    }

    return render(request,'wishlist/show.html', context)

def add_tolist(request, Item_id):
#Adding to the list --------------------------------------------
    print "GOT TO ADD ITEM ROUTE"
    print Item_id

    current_user = User.objects.get(id=request.session['user_id'])
    this_item = Item.objects.get(id=Item_id)
    this_item.listed_by.add(current_user)
    current_user.listed_items.add(this_item)
    this_item.save()
    current_user.save()
    messages.success(request, "You have added an item!")
    return redirect(reverse('wishlist:index'))
        
    messages.error(request, "You didn't add anything!")
    return redirect(reverse('wishlist:index'))



def destroy(request, Item_id):
#To Remove an Item --------------------------------------------
    current_user = User.objects.get(id=request.session['user_id'])
    this_item = Item.objects.get(id=Item_id)
    this_item.listed_by.remove(current_user)
    current_user.listed_items.remove(this_item)
    messages.success(request, "You have deleted your item!")
    return redirect(reverse('wishlist:index'))


def clear(request):
#To Log Out -------------------------------------------------
    del request.session['user_id']
    return redirect('/')

