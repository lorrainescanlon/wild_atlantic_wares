from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review


def all_products(request):
    """A view to return all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    display_category = None

    Review.objects.filter(approved=True)
    """reviews = Product.reviews.filter()"""
    products = Product.objects.annotate(rating=Avg(('reviews__rating')))

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

            if 'menu' in request.GET:
                display_category = request.GET['menu']
            else:
                display_category = products.category.friendly_name

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            if 'menu' in request.GET:
                display_category = request.GET['menu']
            else:
                display_category = products.category.friendly_name

        if 'menu' in request.GET:
            display_category = request.GET['menu']

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Search criteria can not be blank")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                 description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'display_category': display_category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to return data for an individual product"""

    Review.objects.filter(approved=True)
    products = Product.objects.annotate(rating=Avg(('reviews__rating')))
    product = get_object_or_404(products, pk=product_id)

    reviews = product.reviews.all().order_by("-created_on")
    review_count = product.reviews.count()

    """review_count = product.reviews.filter(approved=True).count()"""

    context = {
       'product': product,
       'reviews': reviews,
       'review_count': review_count,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a new product to the shop"""
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)
