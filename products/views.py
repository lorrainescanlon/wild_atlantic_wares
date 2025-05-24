from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Sum
from .models import Product, Category
from reviews.models import Review


def all_products(request):
    """A view to return all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    display_category = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            display_category = request.GET['menu']
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                  direction = request.GET['direction']
                  if direction =='desc':
                     sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

            if 'menu' in request.GET:
                    display_category = request.GET['menu']
            else:
                display_category = product.category.friendly_name

        if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)
                if 'menu' in request.GET:
                    display_category = request.GET['menu']
                else:
                    display_category = product.category.friendly_name
                
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Search criteria can not be blank")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
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

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all().order_by("-created_on")
    review_count = product.reviews.filter(approved=True).count()

    if review_count <= 0:
        product_rating = "No reviews yet"
    else:
        product_rating = int(Review.objects.filter
                             (product=product, approved=True).aggregate
                             (total=Sum('rating'))["total"]/review_count)

    context = {
       'product': product,
       'reviews': reviews,
       'review_count': review_count,
       'product_rating': product_rating,
    }

    return render(request, 'products/product_detail.html', context)
