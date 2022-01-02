from app.forms import CustomerRegistrationForm, CustomerProfileForm
from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.contrib import messages


category  = Category.objects.all()
tutorial  = Tutorial.objects.all()

def home(request):
    context={}
    product = Product.objects.filter(discount__range=(12,16))
    pr = Product.objects.filter(discount__range=(12,16))
    bestProd = Product.objects.filter(rating__range=(50,100))
    bpr = Product.objects.filter(rating__range=(50,100))

    for i in bestProd:
        i.base_price = i.base_price - i.base_price*i.discount//100
    
    for i in product:
        i.base_price = i.base_price - i.base_price*i.discount//100
    list = zip(product, pr)
    list2 = zip(bestProd, bpr)
    context['list'] = list
    context['list2'] = list2
    context['category'] = category
    context['tutorial'] = tutorial
    return render(request, 'app/home.html',context)


def product_detail(request, pk):
    context ={}
    context['category'] = category
    context['tutorial'] = tutorial
    product = Product.objects.get(id=pk)
    pr = Product.objects.get(id=pk)
    product.base_price = product.base_price - product.base_price*product.discount//100
    context['product'] = product
    context['pr'] = pr
    return render(request, 'app/productdetail.html',context)


def add_to_cart(request):
    val = request.GET.get('prod_id')
    user = request.user
    prod = Product.objects.get(id=val)
    Cart(user=user, product=prod).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount =0
        for i in cart:
            i.product.base_price = i.product.base_price - i.product.base_price*i.product.discount//100
            amount = amount + i.product.base_price
        totalamount = amount+70
        return render(request, 'app/addtocart.html', {'cart':cart, 'amount':amount, 'totalamount':totalamount})

def buy_now(request):
 return render(request, 'app/buynow.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "app/profile.html", {"form":form, "active":"btn-primary"})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name= form.cleaned_data['name']
            locality= form.cleaned_data['locality']
            city= form.cleaned_data['city']
            state= form.cleaned_data['state']
            zipcode= form.cleaned_data['zipcode']
            reg = Customer(user=usr, name = name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations Profile Updated Successfully !!")
        return render(request, "app/profile.html",{'form':form, 'active':"btn-primary"})

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',{'add':add, 'active':'btn btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')


def product(request, pk):
    context={}
    product = Product.objects.filter(category=pk)
    pr = Product.objects.filter(category=pk)

    for i in product:
        i.base_price = i.base_price - i.base_price*i.discount//100
    
    list = zip(product, pr)
    context['list'] = list
    context['category'] = category
    context['tutorial'] = tutorial
    
    return render(request, 'app/product.html',context)



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!!! You have been registered successfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})

    


def checkout(request):
    context={}
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_item = Cart.objects.filter(user=user)
    context={'add':add, 'cart_item':cart_item}


    return render(request, 'app/checkout.html', context)

def show_tutorial(request, pk):
    context={}
    exercise = Exercise.objects.filter(tutorial=pk)
    context['tutorial'] = tutorial
    context['category'] = category
    context['exercise'] = exercise
    return render(request, 'app/tutorial.html',context)
    
