
from django.shortcuts import render

from .models import Product, ProductRating

def get_products_filter(price_min, price_max, filter_category):

    # Translate filter cases to queries
    if price_min and price_max and filter_category:
        return Product.objects.filter(
            price__gte=price_min,
            price__lte=price_max,
            category=filter_category
        )

    if price_min and price_max:
        return Product.objects.filter(
            price__gte=price_min,
            price__lte=price_max
        )

    if price_min and filter_category:
        return Product.objects.filter(
            price__gte=price_min,
            category=filter_category
        )

    if price_max and filter_category:
        return Product.objects.filter(
            price__lte=price_max,
            category=filter_category
        )

    if price_min:
        return Product.objects.filter(
            price__gte=float(price_min)
        )

    if price_max:
        return Product.objects.filter(
            price__lte=price_max
        )

    if filter_category:
        return Product.objects.filter(
            category=filter_category
        )

def product_listing(request):

    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    filter_category = request.GET.get("category")

    print(price_min)
    print(price_max)
    print(filter_category)

    print(price_min is None)
    print(price_max is None)
    print(filter_category is None or filter_category == '') 

    #all_products = Product.objects.order_by('-price')

    all_products = []
    if price_min is None and price_max is None and filter_category is None or filter_category == '':
        all_products = Product.objects.all()
    else:
        all_products = get_products_filter(price_min, price_max, filter_category)

    # Results in a list of tuples, extract out the first value
    all_available_categories_state = Product.objects.order_by().values_list("category").distinct()
    all_available_categories = [cat[0] for cat in all_available_categories_state]

    products_with_rating = []

    for product in all_products:
        product_dict = product.to_dict()

        rating = ProductRating.objects.get(product__id=product.id)
        print(rating)

        product_dict["rating"] = rating.to_dict()

        products_with_rating.append(product_dict)
    

    context = {
        "products": products_with_rating,
        "available_categories": list(all_available_categories)
    }

    return render(request, 'products.html', context)
    
def product_single(request, product_id):

    product = Product.objects.get(pk=product_id)

    if product:

        product_dict = product.to_dict()

        rating = ProductRating.objects.get(product__id=product_dict["id"])

        product_dict["rating"] = rating.to_dict()

        product_with_rating = product_dict
        
        context = {
            "product": product_with_rating
        }
        
        return render(request, 'product.html', context)

    else:
        return HttpResponse(status=404)
