
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        # Retrieve the order for the logged-in user
        order = get_object_or_404(Order, pk=pk, user=request.user)

        return render(request, "orders/order_detail.html", {"order": order})


class OrderCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """Handles order creation from the cart when a user submits the checkout form."""

        # Get the user's cart
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = cart.items.select_related("product")  # Optimized DB query

        # Create an order
        order = Order.objects.create(user=request.user)

        # Transfer cart items to the order only if there are items
        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            for item in cart_items
        ]
        if order_items:
            OrderItem.objects.bulk_create(order_items)  # ✅ Bulk insert for efficiency

        # Clear the cart (even if empty, for consistency)
        cart.items.all().delete()

        messages.success(request, "Your order has been placed successfully!")
        return redirect("orders:order_detail", pk=order.pk)



class PaymentProcessView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Fetch the order object
        order = get_object_or_404(Order, id=self.kwargs['pk'], user=request.user)

        # Ensure order is unpaid before proceeding
        if order.paid:
            messages.error(request, "This order has already been paid.")
            return redirect("orders:order_detail", pk=order.id)

        # Integrate Payment Gateway Logic Here (Stripe, PayPal, etc.)
        # Example: For Stripe, create a checkout session, redirect user to payment gateway
        # Redirect to the payment gateway's checkout page (for simplicity, we'll redirect directly)

        return redirect("orders:payment_complete", pk=order.id)  # Replace with actual payment gateway URL



class PaymentCompleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Get order by ID
        order = get_object_or_404(Order, id=self.kwargs['pk'], user=request.user)

        # Ensure the order has not been marked as paid
        if order.paid:
            messages.success(request, "Payment was already processed!")
        else:
            # Update the order as paid
            order.paid = True
            order.save()

            messages.success(request, "Your payment was successful! Thank you for your order.")

        return redirect("orders:order_detail", pk=order.id)
