from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CartView(TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user)

        context['cart'] = cart
        context['items'] = cart.items.all()
        context['total_price'] = cart.total_price()

        return context


@method_decorator(login_required, name='dispatch')
class AddToCartView(TemplateView):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs['slug'])
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # Update the quantity if the product already exists in the cart
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart:cart_detail')


@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(TemplateView):

    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(CartItem, id=kwargs['item_id'])
        cart_item.delete()

        return redirect('cart:cart_detail')


@method_decorator(login_required, name='dispatch')
class UpdateCartView(TemplateView):

    def post(self, request, *args, **kwargs):
        item_id = kwargs['item_id']
        quantity = request.POST.get('quantity')

        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.quantity = int(quantity)
        cart_item.save()

        return redirect('cart:cart_detail')
