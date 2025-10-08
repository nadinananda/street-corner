from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'nama aplikasi' : 'street corner',
        'npm' : '2406351806',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'form': ProductForm(),
    }

    if request.user.is_authenticated:
        date = request.user.last_login 
        context['last_login'] = date

    return render(request, "main.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.select_related("user").all()

    filter_type = request.GET.get("filter", "all")
    if filter_type == "my" and request.user.is_authenticated:
        product_list = product_list.filter(user=request.user)

    data = [
        {
            'id' : str(product.id),
            'name' : product.name,
            'price' : float(product.price) if product.price is not None else None,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category' : product.category,
            'is_featured' : getattr(product, "is_featured", False),
            'user_id'       : product.user_id,
            'user_username' : product.user.username if product.user_id else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try: 
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try: 
        product = Product.objects.select_related('user').get(pk=product_id)

        data = {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price) if product.price is not None else None,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': getattr(product, "is_featured", False),
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }

        return JsonResponse(data)
   except Product.DoesNotExist:
      return JsonResponse({'error': 'Product not found'}, status=404)

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    return render(request, "product_detail.html")

# Tugas 4
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Tugas 5
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

# Tugas 6
@login_required
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({'status': 'success', 'message': 'Product created successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required
def update_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'You are not authorized to edit this product.'}, status=403)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required
@require_POST
def delete_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Forbidden'}, status=403)
    product.delete()
    return JsonResponse({'status': 'success'})

@csrf_exempt
@require_POST 
def login_ajax(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            'status': 'success',
            'message': 'Login successful! Redirecting...',
            'redirect_url': '/' 
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid username or password. Please try again.'
        }, status=400) 

@require_POST
def register_ajax(request):
    data = json.loads(request.body)
    form = UserCreationForm(data)

    if form.is_valid():
        user = form.save()
        login(request, user) 
        return JsonResponse({
            'status': 'success',
            'message': 'Registration successful! Redirecting...',
            'redirect_url': '/'
        })
    else:
        return JsonResponse({
            'status': 'error',
            'errors': form.errors 
        }, status=400)


