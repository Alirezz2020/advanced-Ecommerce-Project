from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import  redirect
from .forms import ReviewForm













class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.all().order_by("-created_at")

        # Get filter parameters from the request
        category = self.request.GET.get("category")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        search_query = self.request.GET.get("q")

        # Apply category filter
        if category:
            queryset = queryset.filter(category__slug=category)

        # Apply price range filter
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        # Apply search filter
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add categories to the context for the filter form
        context["categories"] = Category.objects.all()

        products = self.get_queryset()
        page_number = self.request.GET.get('page', 1)  # Get current page, default to 1
        paginator = Paginator(products, self.paginate_by)
        current_page = paginator.get_page(page_number)

        context['current_page'] = current_page.number
        context['total_pages'] = paginator.num_pages

        return context





class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # ✅ Assign a User instance, not a string
            review.product = self.object
            review.save()
            return redirect('products:product_detail', slug=self.object.slug)
        return self.get(request, *args, **kwargs)



class CategoryListView(ListView):
    model = Product
    template_name = "products/category_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        return Product.objects.filter(category__slug=category_slug).order_by("-created_at")



class BrandListView(ListView):
    model = Product
    template_name = "products/brand_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        brand_name = self.kwargs.get("name")
        return Product.objects.filter(brand__name=brand_name).order_by("-created_at")





