from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Main, Card
from cart.forms import CartAddProductForm
from django.contrib.auth import login, authenticate
from shop.forms import SignUpForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(name__contains=query)

    context = {
        'category': category,
        'categories': categories,
        'products': products,

    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('shop:product_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def main(request):
    last_three = Card.objects.order_by('-id')[:3]
    card1 = last_three[2]
    card2 = last_three[1]
    card3 = last_three[0]
    image = Main.objects.reverse()[0]
    context = {
        'card1': card1,
        'card2': card2,
        'card3': card3,
        'image': image

    }
    return render(request, 'shop/main.html', context)


def about(request):
    return render(request, 'shop/about.html')


def opt(request):
    return render(request, 'shop/opt.html')


def contact(request):
    return render(request, 'shop/contact.html')


def payship(request):
    return render(request, 'shop/payship.html')
