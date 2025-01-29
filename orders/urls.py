from django.urls import path
from .views import *

app_name = "orders"

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("detail/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
  path("payment/process/<int:pk>/", PaymentProcessView.as_view(), name="payment_process"),
    path("payment/complete/<int:pk>/", PaymentCompleteView.as_view(), name="payment_complete"),

]
