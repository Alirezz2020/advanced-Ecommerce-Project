from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail/', views.CartView.as_view(), name='cart_detail'),
    path('add/<slug:slug>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:item_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('update/<int:item_id>/', views.UpdateCartView.as_view(), name='update_cart'),
]
