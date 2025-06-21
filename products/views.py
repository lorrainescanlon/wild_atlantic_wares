from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

            """if 'menu' in request.GET:
                display_category = request.GET['menu']
            else:
                display_category = products.category.friendly_name"""

        if 'category' in request.GET:
            """display_category = request.GET['category'].friendly_name"""
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            """if 'menu' in request.GET:
                display_category = request.GET['menu']
            else:
                display_category = products.category.friendly_name"""

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


@login_required
def add_product(request):
    """ Add a product to the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised users can manage Products')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.'
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised users can manage Products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised users can manage Products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted Successfully')
    return redirect(reverse('products'))
