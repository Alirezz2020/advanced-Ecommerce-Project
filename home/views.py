
from django.views.generic import TemplateView, ListView
from products.models import Product, Category, Brand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.order_by('-created_at')[:6]  # Latest 6 products
        context['categories'] = Category.objects.all()  # All categories
        context['brands'] = Brand.objects.all()[:6]  # Top 6 brands (customize as needed)
        return context





class SearchView(ListView):
    model = Product
    template_name = "task_search_results.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            ).order_by("-created_at")
        return Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        page_number = self.request.GET.get("page", 1)
        paginator = Paginator(queryset, self.paginate_by)

        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            products = paginator.page(1)  # If the page is not an integer, show the first page
        except EmptyPage:
            products = paginator.page(paginator.num_pages)  # If page is out of range, show the last page

        context["products"] = products
        context["query"] = self.request.GET.get("q", "")
        return context
