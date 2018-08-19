from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Main, Card, Text
from cart.forms import CartAddProductForm
# from django.contrib.auth import login, authenticate
# from shop.forms import SignUpForm
# from django.shortcuts import redirect


def categories(request, category_slug=None):
    categories = Category.objects.all()

    context = {
        'categories': categories,

    }
    return render(request, 'shop/product/categories.html', context)


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
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('shop:product_list')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


def main(request):
    if Card.objects.order_by('-id')[:3]:
        last_three = Card.objects.order_by('-id')[:3]

        card1 = last_three[2]
        card2 = last_three[1]
        card3 = last_three[0]
    else:
        card1 = None
        card2 = None
        card3 = None
    image = Main.objects.reverse()[0]
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'card1': card1,
        'card2': card2,
        'card3': card3,
        'image': image

    }
    return render(request, 'shop/main.html', context)


def about(request):
    text = Text.objects.get(pk=1)
    categories = Category.objects.all()
    context = {
        'text': text,
        'categories': categories,
    }
    return render(request, 'shop/about.html', context)


def payship(request):
    categories = Category.objects.all()
    text = Text.objects.get(pk=2)
    context = {
        'text': text,
        'categories': categories,
    }
    return render(request, 'shop/payship.html', context)


def contact(request):
    categories = Category.objects.all()
    text = Text.objects.get(pk=3)
    context = {
        'text': text,
        'categories': categories,
    }
    return render(request, 'shop/contact.html', context)


def opt(request):
    categories = Category.objects.all()
    text = Text.objects.get(pk=4)
    context = {
        'text': text,
        'categories': categories,
    }
    return render(request, 'shop/opt.html', context)
